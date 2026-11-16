# OverSpec changes

## 0.6.20261118 (beta)

Online play for two, faster tape loading, and two Windows fixes.

- **Two players online (first version, from the command line).** One player
  starts `overspec GAME --host` and gets a six-letter code; the other starts
  `overspec GAME --join CODE` with the same game file and the same OverSpec.
  Both machines begin the game afresh and then run the same frames on both
  players' keys and joysticks, so either player can press anything. Key
  presses travel through a small meeting point run by OverSpec's author on
  Cloudflare; the game itself is never sent. Rewind, loading a save and
  restart are off while a game is shared, and it stops with a message if the
  two machines ever differ. Windows and Linux copies have been checked to
  compute identical machines; nobody has yet played it between two homes,
and it has no menu entry yet.
- **More tapes load at once.** OverSpec loads a block instantly when a
  program reads it with the Spectrum's own loader. It used to do so only
  when the block was exactly the length asked for. It now reads whatever the
  loader would have read, stops where the loader would have stopped, and
  lets the tape play on from there, so a block with a stray byte after it, a
  block the program is skipping, and ordinary blocks stored in a tape file
  pulse by pulse all load at once. So does a block shorter than what the
  program asked for, which many games rely on and ignore the error (Sir
  Fred, Minder, Iron Lord). Across the TOSEC set this cuts the time spent in
  the Spectrum's loader at cassette speed by nearly three quarters, and some
  tapes that used to stop part way now load: Critical Mass, Fairlight,
  Kung-Fu Master, International Rugby, Turrican II and The NeverEnding
  Story among them.
- **Windows: update checks and reports now get through.** An installed
  Windows copy could not make a secure connection: its web library looked
  for a list of trusted certificates in a place that exists only on the
  machine that built it. So on Windows the daily check for a new version
  never found one, and a crash or problem report you chose to send was not
  delivered. OverSpec now trusts the certificates Windows trusts. Because
  of this, a Windows copy older than this one will not offer this update:
  install it by hand once. Every Windows build from 0.6.20261114 to
  0.6.20261117 is affected. Nobody reported it; it was found while testing
  online play between a Windows and a Linux machine.
- **Windows: disk timing no longer runs out after ten minutes.** On Windows
  the disk controllers counted time in a number that overflowed after about
  ten minutes of play. From then on a TR-DOS disk's index mark read as
  always present, and a disk read begun at the wrong instant could be cut
  short. Time is now counted the same way on every system. Found while
  checking that a Windows and a Linux machine stay identical for online
  play; nobody reported it.
- **Save picture.** In a game, Menu > Picture & sound > Save picture saves
  what the game is showing as a PNG, three times its size so the pixels stay
  sharp, in the pictures folder beside your saves and settings.

## 0.6.20261117 (beta)

Three tape fixes, found by running the whole TOSEC set again after each one.

- **Tapes: data arrives the right way up.** A Spectrum writes each bit as a
  low pulse and then a high one, and a few loaders read those levels instead
  of the edges between them. A tape file records only pulse lengths, so
  whether a block came out upright depended on how many pulses its lead-in
  tone had. Blocks that would have played upside down are now turned over.
  Basil the Great Mouse Detective loads on all six of its tapes, and Lone
  Wolf III side B now reaches its title.
- **Tapes: the silence between blocks behaves as it does on a real deck.**
  A pause on a tape is now the low level after its first millisecond, and a
  tape that stops part way through a pause lets the rest of it pass in real
  time instead of skipping it. Sam Stoat Safebreaker (Speedlock 1) looks at
  the tape in that silence before it starts reading, and now loads. Skipping
  the silence also moved the next tone against the program, which Speedlock 2
  is sensitive to: Head over Heels loaded only by luck, and no longer depends
  on it. A few tapes now wait out a pause that used to be skipped.
- **Known:** P.H.M. Pegasus (Electronic Arts tape) decrypts itself with
  whatever an unattached port returns at the moment loading ends, which
  depends on where the picture is being drawn. It loaded in 0.6.20261116 and
  may not in this build. The Dro Soft release loads. One cracked tape of
  Beach-Head II has a sync pulse right on its loader's limit and is in the
  same position. A resume point saved by
  an older build while a tape was in the last millisecond of a pause hears
  that pause once more.

## 0.6.20261116 (beta)

- **Record and share replays of Spectrum Next games.** While a Next game is
  running, Pause > Picture & sound > Record Next replay records what you play,
  for up to an hour. Rewind while recording and the replay continues from
  where you rewound to, so a mistake does not end the take. The replay then
  plays as that game's preview in the library. Export replay saves it as an
  `.rzx` file someone else can bring in with Import replay, provided they
  have the same game: the file holds your key presses and the machine's
  memory at the start, as a classic Spectrum RZX does, and not the game file.
  Every replay is checked frame by frame, picture and sound, before it is
  kept. Games started through NextZXOS can be recorded but not shared.
- **OverSpec tells you about new versions.** Once a day, while it is open, it
  asks its GitHub page whether there is a newer build. When there is, it asks
  what to do: update now, later, or skip that version. Update now downloads
  the package for your system, checks it against the size and SHA-256 listed
  for the release, and installs it: on Windows it starts the setup program, on
  Linux it updates a copy installed with `install.sh`, and on a Mac it opens
  the disk image. A copy that was only unzipped is sent to the download page
  instead. Nothing is downloaded or installed without a yes, and it never asks
  while a game is on screen. The check sends nothing but the request itself,
  which carries the OverSpec version; it can be turned off in Settings >
  Updates > New version alerts.
- **The update check now sees test builds.** Earlier builds looked for
  GitHub's "latest" release, which leaves out builds marked as pre-releases,
  as every OverSpec build so far is. Settings > Updates always answered that
  there was no public release.
- **Settings and saves on Windows** (reported in issue 2): OverSpec could
  not create or use its settings folder when it was started from the top of
  a drive, or installed on a different drive from that folder. Nothing could
  be saved, and choosing another folder answered "OverSpec cannot write to
  that folder". Fixed. A `--data-dir` folder written with backslashes is
  now created too.
- **Compatibility, from a run of 42,427 Spectrum files.** Every file in the
  2012 TOSEC Spectrum set was run and compared with another emulator. Three
  faults that came out of it are fixed:
  - Games that write to port $FF by accident no longer get a garbled
    picture (Hawk Storm, Full Throttle II, World Cup Challenge, Pulsator and
    about thirty more). Only a Timex has its screen mode on that port; a
    tape written for a Timex is started on a TC2048 instead.
  - A tape now waits in the silence between two blocks while nothing is
    reading it, as a person at the tape deck would. Combat School, Athena
    and Road Runner load where they used to stop at a black screen.
  - A +3 disk laid out as a CPC's is started from its boot sector (Tintin
    on the Moon).
- **Choosing a folder on Windows** (reported in issue 1): going up from the
  top of a drive now leads to Locations, which lists every drive with its
  name and any network folders in use. A network folder such as
  `\\server\share` can be browsed like any other.
- **Command line, for front ends such as LaunchBox:** `overspec GAME` has
  always started a game. `--fullscreen` starts full screen for that run, and
  `--quit-with-game` closes OverSpec when the game is left, so a front end
  gets control back.

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
