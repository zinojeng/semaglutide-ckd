#!/usr/bin/env bash
set -euo pipefail

project_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_dir="$project_root/fulltext"

usage() {
  echo "USAGE: $0 lock|verify|unlock --confirm" >&2
}

verify_locked() {
  if [[ ! -d "$source_dir" ]]; then
    echo "SOURCE_CORPUS_ABSENT fulltext/ (expected in public clones)"
    return 0
  fi

  local failed=0
  if [[ -w "$source_dir" ]]; then
    echo "SOURCE_CORPUS_WRITABLE_DIRECTORY fulltext/" >&2
    failed=1
  fi

  while IFS= read -r -d '' path; do
    if [[ -w "$path" ]]; then
      echo "SOURCE_CORPUS_WRITABLE_FILE ${path#"$project_root/"}" >&2
      failed=1
    fi
  done < <(/usr/bin/find "$source_dir" -type f -print0)

  if [[ "$failed" -ne 0 ]]; then
    return 1
  fi
  echo "SOURCE_CORPUS_LOCKED fulltext/"
}

case "${1:-}" in
  lock)
    if [[ "$#" -ne 1 ]]; then
      usage
      exit 2
    fi
    if [[ ! -d "$source_dir" ]]; then
      echo "SOURCE_CORPUS_ABSENT fulltext/"
      exit 0
    fi
    /usr/bin/find "$source_dir" -type f -exec /bin/chmod a-w {} +
    /bin/chmod a-w "$source_dir"
    verify_locked
    ;;
  verify)
    if [[ "$#" -ne 1 ]]; then
      usage
      exit 2
    fi
    verify_locked
    ;;
  unlock)
    if [[ "${2:-}" != "--confirm" || "$#" -ne 2 ]]; then
      echo "Refusing to unlock without the explicit --confirm flag." >&2
      usage
      exit 2
    fi
    if [[ ! -d "$source_dir" ]]; then
      echo "SOURCE_CORPUS_ABSENT fulltext/"
      exit 0
    fi
    /bin/chmod u+w "$source_dir"
    /usr/bin/find "$source_dir" -type f -exec /bin/chmod u+w {} +
    echo "SOURCE_CORPUS_UNLOCKED fulltext/"
    ;;
  *)
    usage
    exit 2
    ;;
esac
