# SeriesWeave

Mix and match your favorite shows in one playlist — never get bored watching the same series for hours

![Demo](preview.gif)

## Features

- 🎲 Randomly shuffles between series while maintaining episode order
- 💾 Save and resume playlist progress
- 🎬 Support for multiple video players (VLC, MPC-HC, KMPlayer)
- 📁 Automatic season detection
- ⚙️ JSON-based configuration
- 🖥️ Windows MessageBox UI for user interaction

---

## Installation

### Download .exe (Windows)

1. Download `SeriesWeave.exe` from [Releases](https://github.com/SGK1ng/SeriesWeave/releases)
2. Place it in any folder
3. Run and configure `config.json`

### Optional: Add to "Send To" Menu

1. Press `Win + R`, type `shell:sendto`, press Enter
2. Copy `SeriesWeave.exe` (or create a shortcut) to the opened folder

---

## Configuration

Edit `config.json` (created on first run):

```json
{
  "player_path": "C:/Program Files/VideoLAN/VLC/vlc.exe",
  "save_path": "./playlist_save.txt",
  "video_extensions": ["mp4", "avi", "mkv"]
}
```

---

## Usage

**Run with directory:**

````bash
SeriesWeave.exe "C:/path/to/series"
```

**Folder structure:**
```
Series/
├── Breaking Bad/
│   ├── Season 1/
│   │   ├── episode1.mp4
│   │   └── episode2.mp4
│   └── Season 2/
└── The Office/
    └── Season 1/
````

The app will create a shuffled playlist like:

1. Breaking Bad S01E01
2. The Office S01E01
3. Breaking Bad S01E02
4. The Office S01E02 ...
