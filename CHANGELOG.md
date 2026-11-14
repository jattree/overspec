# OverSpec changes

## 0.6.20261115 (beta)

More of the Spectrum's extra display hardware, checked against a test set of
about 1,200 programs gathered for the purpose.

- **A new look, made for a controller:** the library is now a full-screen
  interface with artwork behind it, shelves of cards and a moving highlight.
  Everything can be done with a game controller and no keyboard or mouse:
  browsing, search (with an on-screen keyboard), choosing folders and files,
  NextZXOS setup, the pause menu, a Spectrum keyboard in the game, Spec256
  recolouring with undo, and the questions the player asks. The keyboard and
  mouse still work everywhere, and the hints at the bottom follow whichever
  you last used. It has been tested with simulated controllers; reports from
  real ones are welcome.
- **Cards:** each card shows the cassette front, and the one in focus turns
  to its loading screen.
- **Full screen is remembered** from one run to the next.
- **Previews you can hear:** the gameplay previews in the library now play
  their sound as well as their picture. The speaker button beside More turns
  it off and on, and your choice is remembered.
- **Games in the box:** OverSpec now comes with games, demos and patches for
  every kind of display it plays: Timex, multicolour, ULAplus, the ZX-Uno,
  Gigascreen, SPECTRA, Spec256 games in 256 colours, and NexClash `.nxc`
  patches (a patch needs your own copy of its game). Each has a picture.
  `games/CREDITS.txt` lists whose they are and what is recorded about passing
  each one on; if one is yours and you want it gone, open an issue. They
  are optional: the
  Windows setup program has a tick box for each kind, and on Linux
  `install.sh --no-games` leaves them out. Their saves are kept in your own
  data folder like any other game's.
- **ULAplus:** programs that change the palette while the picture is being
  drawn now look right. The HAM 8x1 picture viewer showed streaks; it is clean.
- **Multicolour and border effects:** the 16K to +3 machines now draw the
  picture as the beam crosses the screen, eight pixels at a time, where before
  a change part way across a line was applied to the whole line.
- **SPECTRA:** new. The SPECTRA interface's 64 colour modes on the 48K machine,
  with its finer attributes, enhanced border and second screen.
- **Timex machines:** new. The Timex TC2048 and the Timex Sinclair 2068 are
  now machines of their own, with the 2068's sound chip, joystick and sixty
  frames a second. Its cartridges (`.dck`) play, its tapes load at once like
  a Spectrum's, and both machines are in the machine list. A tape with TS2068,
  TC2068 or TC2048 in its file name starts on the right one; for any other
  Timex tape, choose the machine from that list.
- **Timex programs started on a Spectrum:** a tape that turns out to be
  written for a Timex, with nothing in its name to say so, now restarts on a
  Timex TC2048 by itself. Hi-Color Hero and River Raid II showed stripes; they
  now show their full colour.
- **Tapes that skip a block:** when a loader chooses not to load one of its
  blocks, the tape no longer plays that block at its real length. Some titles
  sat on a still screen for a minute before starting.
- **Pictures:** screen files can be opened and shown: standard `.scr`,
  Gigascreen `.img` and MultiArtist `.mg1` to `.mg8` (the two pictures are
  mixed), and multicolour `.mlt`, `.mc` and Timex hi-colour and hi-res `.scr`.
  The library can list all of these except plain loading screens, which
  would bury the games; those open from "Browse files and folders". Pictures
  stay out of the list until you tick them in the Show menu, and each says
  what kind of picture it is.
- **ZX-Uno programs that read files:** a Spectrum program that loads its data
  from an SD card through esxDOS now finds the files beside it. Return to
  Holy Tower plays.
- **A tidier library header:** the row of filter buttons is now one Show
  control and a More menu. Show is a list of tick boxes: 16K, 48K, 128K and
  Spectrum Next, with Spec256, ZX-Poly, ULAplus, Radastan, SPECTRA,
  Gigascreen and Timex under 48K and `.nxc` under Next. Tick a machine to tick everything under it, or open it and tick only
  what you want. Each row says how many games you have of that kind, or that
  you have none, and what you tick is remembered. A game is filed under its machine
  when its details, its snapshot or its file name says which one it is for;
  one that says nothing is listed under both 48K and 128K. More holds Open a
  file, Browse files and folders, Refresh library, Settings and About.
- **Games that say what they are:** once you have played a game that uses
  ULAplus, the ZX-Uno's Radastan mode, SPECTRA, Gigascreen or a Timex screen
  mode, the library names it for that and files it under that row of the
  Show menu. OverSpec learns this by watching the game run, so a game you
  have not played yet is still listed as a plain Spectrum game.
- **Fixed: choosing a machine.** Picking 128K, +2, +2A, +3 or Pentagon in the
  machine list did nothing. It now restarts the game on that machine.
- **128K titles:** a tape that says nothing about its machine but uses 128K
  memory now starts on a 128K machine, as do files named with `(128)` or
  `128 Kb`. Several titles that sat on a black screen now run.

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
