#!/usr/bin/env bash
# Generates tracks.json listing audio files under this music folder.
cd "$(dirname "$0")" || exit 1
# Find mp3/wav/flac files, sort, and output JSON array with paths prefixed by 'music/'
mapfile -t files < <(find . -type f \( -iname '*.mp3' -o -iname '*.wav' -o -iname '*.flac' \) -printf '%P\n' | sort)
if [ ${#files[@]} -eq 0 ]; then
  echo '[]' > tracks.json
  echo "Generated empty tracks.json"
  exit 0
fi
{
  echo '['
  for i in "${!files[@]}"; do
    f=${files[$i]}
    # encode URI component to handle spaces and special characters
    encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote('music/' + sys.argv[1]))" "$f")
    printf '  "%s"' "$encoded"
    if [ $i -lt $(( ${#files[@]} - 1 )) ]; then
      echo ','
    else
      echo
    fi
  done
  echo ']'
} > tracks.json
echo "Generated tracks.json with ${#files[@]} entries."

# Also generate tracks-inline.js so the page can work via file:// (no server).
{
  echo 'window.TRACKS_INLINE = ['
  for i in "${!files[@]}"; do
    f=${files[$i]}
    encoded=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote('music/' + sys.argv[1]))" "$f")
    printf '  "%s"' "$encoded"
    if [ $i -lt $(( ${#files[@]} - 1 )) ]; then
      echo ','
    else
      echo
    fi
  done
  echo '];'
} > tracks-inline.js
echo "Generated tracks-inline.js with ${#files[@]} entries."
