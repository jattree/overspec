# OverSpec changes

## 0.6.20261113 (early test build)

Added

- **Mac:** the first Mac build, as separate packages for Apple Silicon and
  Intel, for macOS 13 or later. It has had far less testing than the Windows
  and Linux builds. It also carries fixes that reach Windows and Linux in
  the next build: quitting when a save fails keeps the game open and offers
  Retry, and a second resume point set aside no longer replaces the first.

Fixed

- **Windows:** games in folders with accented or non-Latin names now open.
- **Linux:** updating no longer removes a saves folder kept inside the program
  folder, and the applications menu entry works when the install path has a
  space in it.
- A controller button held while opening the library no longer stays pressed
  when you go back to the game.
- Your place in a game saved by an older version is now kept beside the new
  one, not written over. You are told if your place could not be saved.
- Renaming or moving your games folder: saves now follow reliably, and Next
  games set up to start through NextZXOS keep working.
- Colours painted on one Spec256 game no longer show up in another.
- A game's start mode (NextZXOS or Fast) no longer changes when you launch a
  different game.
- An interrupted save to a Next game's SD card no longer loses the saves
  before it.
- Damaged tape files, damaged save files and badly behaved Next programs can
  no longer crash the player.

## 0.6.20261112 (early test build)

The first public test build, for Windows and Linux.
