Instrukcja dodawania utworów

- Umieść pliki MP3 (lub inne obsługiwane pliki audio) w tym katalogu `music/`.
- Zaktualizuj plik `tracks.json`, dodając nazwy plików w kolejności, w jakiej chcesz, by były odtwarzane. Przykład:

[
  "moj_plik1.mp3",
  "inny_utwor.mp3"
]

- Uruchom serwer HTTP z katalogu nadrzędnego (lub otwórz stronę), np.:

```bash
cd /home/filip/Documents/ht
python3 -m http.server 8000
```

- Otwórz: http://localhost:8000/glowne

Uwaga: pliki nie są przesyłane nigdzie — są serwowane ze strony właściciela. Jeśli chcesz, mogę dodać prosty skrypt (np. `build_playlist.sh`), który automatycznie zindeksuje pliki w tym folderze i wygeneruje `tracks.json`.