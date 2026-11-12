# OverSpec changes

## 0.6.20261114 (early test build)

This build answers a report from someone whose first run went badly. Each
point they raised is listed here.

From that report

- **"It indexed my whole hard drive."** A whole disk, a system folder or your
  entire home folder is no longer accepted as a games folder. You are asked to
  choose the folder your games are in.
- **"It claimed millions of games."** A scan now stops at 300,000 files and
  says the folder holds too much, and the library says when not everything is
  shown.
- **"It was slow."** Starting with a large library is far quicker: a library
  of 70,000 files that took about two minutes to open now takes about a second.
- **"It crashed."** We could not make this crash happen ourselves. The limits
  above remove the likeliest cause, and this build can now tell us when it
  fails (see Reports, below).
- **"The file requester ignores my system's display and accessibility
  settings."** Choosing a games folder and opening a game now use your
  system's own dialog: the Windows one, the macOS one, or zenity or kdialog on
  Linux. OverSpec's own file list is still there under Files. The rest of
  OverSpec's screens are still drawn by OverSpec and do not yet follow system
  accessibility settings.

Reports (new)

- If OverSpec crashes or stops responding, the next start asks whether to send
  a report. Nothing is sent unless you say yes. The report holds the OverSpec
  version, your type of system, the name of the last game started and where
  the program failed.
- **Report a problem**, in the in-game menu and in Settings, for a wrong
  picture, wrong sound, controls, or something slow or stuck. It shows what
  will be sent before you choose: the version, your type of system, the game's
  file name, your display settings, how many games are in your library, how
  long the last scan took and, from inside a game, the picture the game is
  showing. The library screen is never sent.
- Reports go to a server run by OverSpec's author. No account is needed and
  your internet address is not kept with them.

Also fixed

- Dropping a different folder on the window while a version picker was open
  could crash.
- **Windows:** choosing the top of a drive in the system dialog is refused as
  a whole disk, as it should be.
- **macOS:** separate Intel and Apple Silicon packages, with architecture checks
  for every bundled executable and library and dependencies built for macOS 13.
- **macOS:** the package declares the minimum macOS version required by its
  actual programs and libraries, instead of always claiming macOS 12.
- **macOS:** fonts, themes and preparation scripts are packaged as resources,
  so the app's signature survives a copy that does not preserve extended attributes.
- Quitting after a failed save now offers Cancel, Retry, or Quit without saving
  before closing the game. The previous save stays intact.
- Moving a games folder: a prepared Next launch whose path could not be saved
  is retried on the next library refresh, before moving the game's saves.
- A second resume point set aside no longer replaces the first.
- **Linux:** an update that fails part way through copying leaves the
  installed program as it was.

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
