# OverSpec user guide

OverSpec plays ZX Spectrum games, from the 16K to the Spectrum Next, along with
Spec256, ZX-Poly and NexClash `.nxc` editions. Playing a game leaves its file
unchanged.

## Contents

- [Quick reference](#quick-reference)
- [Getting started](#getting-started)
- [The library](#the-library)
- [Playing a game](#playing-a-game)
- [Saved positions and rewind](#saved-positions-and-rewind)
- [Picture and sound](#picture-and-sound)
- [Versions of a game](#versions-of-a-game)
- [Playing online](#playing-online)
- [The Spectrum Next](#the-spectrum-next)
- [For programmers](#for-programmers)
- [Options and the command line](#options-and-the-command-line)
- [Your files, updates and reports](#your-files-updates-and-reports)

## Quick reference

| What | Where |
|---|---|
| Rewind a few seconds | F6, or Rewind 5 seconds in the game's menu |
| Save and restore a position | F5 and F9 |
| Carry on where you left off | Player settings, Resume games |
| The Spectrum's keyboard on screen | F3 |
| Joystick and keys | F4, or Controls in the game's menu |
| Two players online | Play online in the game's menu |
| Cheats and game options | Game options in the game's menu |
| Pixels, upscaling, colour boost | Picture & sound in the game's menu |
| Boot NextZXOS from your own SD card image | More, Settings, NextZXOS |
| The Next's Raspberry Pi and WiFi | More, Settings, NextZXOS, Pi and WiFi |
| Copper, DMA and sprite marks, layers, sound sources | Picture & sound, Developer view (Next games) |
| The Next's whole 640 × 256 picture | Developer view, Picture: whole display |
| The debugger | F12 in a Spectrum or Next game |
| Options kept in a file | `overspec.ini`, see [Options and the command line](#options-and-the-command-line) |

## Getting started

Start OverSpec and choose the folder that holds your games. Choosing a whole drive
can make the first look through it slow. You can also drop a folder or a single
game onto the window.

OverSpec reads tapes (`.tap`, `.tzx`), snapshots (`.z80`, `.sna`, `.szx`), disks
(`.dsk`, `.trd`, `.scl`) and Next files (`.nex`, `.snx`), among others. For Beta
disk games, put `trdos.rom` in your games folder or give it with `--trdos`.

If your copy came with a `games` folder, its games, demos and patches appear beside
yours, one folder for each kind of display: Timex, multicolour, ULAplus, the ZX-Uno,
Gigascreen, SPECTRA, Spec256 and NexClash patches. See `games/CREDITS.txt` for
credits. An update can replace that folder, so keep your own games elsewhere. To
leave the games out, untick them in the Windows setup, or run
`install.sh --no-games` on Linux.

If looking through your games folder takes a long time, OverSpec opens from the
list it made last time. Choose More, Refresh library after adding or removing games.

## The library

| Key | Controller | Does |
|---|---|---|
| Arrows | D-pad, left stick | Move |
| Enter | A | Play |
| Escape | B | Back |
| I | Y | The game's details |
| Space | X | Favourite or not |
| Page Up, Page Down | Shoulder buttons | Jump by letter |
| / | | Search |
| F | Back or Select | Show |
| M | Start | More |

With the mouse, one click on a game's card opens its details and a double click plays it. In the list view, a click chooses a row and Enter plays it.

Search has an on-screen keyboard for a controller; with a keyboard, type and press
Enter. **Show** chooses which kinds of game are listed. Favourites and Recent have
their own views. Pictures are left out unless you tick them in Show.

**More** has:

| Item | Does |
|---|---|
| Open a file... | Play a game outside your games folder |
| Browse files and folders | OverSpec's own file browser |
| Refresh library | Look through your games folder again |
| Full screen | Full screen or a window |
| Settings | Settings, the same as Player settings in a game |
| About OverSpec | The version |
| Quit OverSpec | Quit |

On Linux the system's file dialogs need zenity or kdialog. With a controller,
OverSpec uses its own file browser.

## Playing a game

| Key | Does |
|---|---|
| Escape or F2 | The game's menu (controller: Guide, or Start and Select together) |
| F1 | Back to the library; F1 again returns to the game |
| F3 | The Spectrum's keyboard on screen |
| F4 | Controls |
| F5 | Save a position |
| F6 | Rewind |
| F9 | Restore the saved position |
| F10 | Pause, and carry on |
| F11 | Full screen |
| F12 | The debugger (Spectrum and Next games) |

The arrow keys work the joystick, and Tab or right Alt fires. Shift is Caps Shift
and Ctrl is Symbol Shift. Controls chooses the joystick: Kempston, Cursor, Sinclair
1, Sinclair 2 or QAOP. A controller's buttons can be set for each game.

On the on-screen keyboard (F3) with a controller, A presses the chosen key, X and Y
choose Caps Shift and Symbol Shift, the shoulder buttons are Space and Enter, and B
closes it.

The game's menu has Resume game, Save position, Restore position, Rewind 5 seconds,
Restart game, Controls, Spectrum keyboard, Picture & sound, Game options, Player
settings, Play online, Full screen and Back to library.

## Saved positions and rewind

F5 saves a position and F9 restores it. Each game has one saved position for each
way of starting it. F6 rewinds a few seconds. Press it again to go further back.

With **Resume games** on (Player settings), a game you have played for more than
five seconds or so starts again where you left it the next time. The resume point
is written when you start another game or quit OverSpec. F1 only switches to the
library, and the game stays where it is.

**Restart game** starts again from the beginning and forgets the resume point. Your
F5 position is kept.

A Next game started directly can keep its own files, such as high scores and
settings. They go in `files/` in your data folder, and the game's own files are not
changed. Restoring a position or rewinding leaves those files as they are.

## Picture and sound

Picture & sound in the game's menu has:

| Item | Does |
|---|---|
| Colour boost | Stronger colours, in steps |
| Display | How many times a second the picture is drawn. It does not change the game's speed |
| Sound | On or off |
| Pixels | Whole-number sizes, or as large as the screen allows |
| Upscaling | Original pixels, Smooth, Scale2x or Scale4x |
| Surround | Fit at 4:3, fill the screen, or the game's artwork round it |
| Display test | A row of 30 marks along the bottom, one lit each second, to see that the picture keeps time |
| Machine model, or Start mode | The Spectrum model a game runs on, or how a Next game starts, where there is a choice. Changing it restarts the game |
| Recolour game | Spec256 games: paint new colours onto the graphics |
| Record preview | Record a short clip of the game for its card in the library. Needs FFmpeg with libx264 |
| Record Next replay, Export replay, Import replay | See below |
| Save picture | The picture as a 960 × 720 PNG in `pictures/` in your data folder |
| Developer view | Next games: see [The Developer view](#the-developer-view) |

**Record Next replay** records a `.nex` game as you play it, and **Stop Next replay**
ends it. OverSpec then checks that it plays back the same. A replay of a `.nex`
started directly can be exported as an `.rzx` file; whoever imports it needs the
same `.nex` in their library. Replays made through NextZXOS stay on this computer.

**Player settings** has Appearance, Preferred version, Fullscreen on play, Resume
games, Picture surround, Upscaling and Start-up ident, and leads to Updates,
NextZXOS, Storage and Report a problem.

## Versions of a game

Some games come in more than one version: the original, a Spec256 edition in 256
colours, a ZX-Poly edition, a Spectrum Next version, or a NexClash `.nxc` patch for
the Next. They are listed as one game, and OverSpec asks which to play. **Preferred
version** in Player settings chooses the one it starts without asking, when it is
there. Kinds that Show hides are left out of a game's versions.

A NexClash patch needs your own copy of the release it was made for, beside the
patch file. To get a patch, open Updates, choose **Download patch + notes**, then
**Add to library**: OverSpec finds your matching original and puts the patch beside
it. In a patched game, **Game options** has switches marked On and Off that change
the game as you play, and Setup items that need a restart; save a position first.

## Playing online

Both players need the same game file and the same version of OverSpec, and both
start the game first.

Starting the shared game restarts it on both computers and clears both automatic
resume points. Press F5 first if you want to keep your place.

1. One player opens the game's menu, chooses **Play online**, then **Host a game**,
   and gives the other player the six-character code it shows.
2. The other player chooses **Play online**, then **Join a game**, and types the
   code.

For a Next game started through NextZXOS, the host first chooses Picture & sound,
Start mode, Fast start; the other player is given the host's set-up.

Once joined, both players' keys and joysticks work in the same game on both
screens, after the first few seconds. Rewind, restoring a position and restarting
are off while the game is shared. **Stop hosting** gives up waiting for the other
player, and **Leave the online game** ends it.

The connection goes through a relay on Cloudflare run by OverSpec's author. It can
see your IP address. It passes the controls and the checks that keep both games in
step between the two players. It never receives the game file and does not record
the game.

From the command line: `overspec GAME --host` and `overspec GAME --join CODE`.

## The Spectrum Next

### Starting Next games

A `.nex` file starts straight away (Fast start), with the registers and memory set
as NextZXOS sets them for a program it starts. A game prepared for NextZXOS can start
through it instead (see below). A `.snx` file is a 48K or 128K snapshot that
runs on the Next with the Next's own hardware on.

### NextZXOS from your own card

To boot the Next's own system, open More, Settings, NextZXOS. Choose the Next's boot
ROM (exactly 8,192 bytes) and a raw SD card image, then Boot NextZXOS, which keeps
them and starts it (Done keeps them without starting). OverSpec supplies neither:
they are your own files. At the welcome
screen press Space, then Enter to open the Browser. F1 switches between NextZXOS
and your library.

Your card image is never written to. What NextZXOS and its programs change on it is
kept in `sd/` in your data folder, and a saved position or rewind includes it.

**Prepare games on Play** starts `.nex` and `.nxc` games from the library through
NextZXOS, as on the machine. It needs the NextZXOS 26.11a card image with its
matching boot ROM, and Python 3, mtools and GNU `cp` on this computer.

### The picture rate and timing

A Next program, or NextZXOS from its settings, can ask for 60 Hz, or for the 48K's
or the Pentagon's timing in place of the +3's. OverSpec follows. The Pentagon's
timing stays at 50 Hz, and 60 Hz runs at about 59 frames a second, as on the
machine.

### The clock

The Next's clock uses this computer's local time, set when a Next program starts or
a saved position is restored. A program cannot set it. There is no clock in an
online game.

### The SD card's speed

The Next's SD card answers at once. To try a program at a real card's pace, start
OverSpec with `--sd-speed slow`, `normal` or `fast` (the rates of slow, typical and
fast real cards), or `--sd-speed READ,WRITE` in bytes a second, each from 1,000 to
100,000,000. `unlimited` is the default. It applies to NextZXOS booted from its
card; a `.nex` started directly reads its files at once.

### WiFi

The Next's WiFi module can work through this computer's network. Open More,
Settings, NextZXOS, Pi and WiFi, and set **WiFi module** to On, or start OverSpec
with `--esp-wifi`. It is off until you turn it on.

With it on, a Next program can reach other computers on your network and on the
internet, but not this computer itself unless OverSpec is started with
`--esp-wifi-local`. It can open up to five TCP, UDP or SSL links, look up names,
ping and give the time, and it can open a listening TCP port on this computer for
others to connect to. SSL encrypts the link, but OverSpec does not check the
server's identity, as the real module does by default. The links it makes, and those it
refuses, are printed in the terminal OverSpec was started from.

The module is joined to a network called OverSpec and starts at 115200 baud. It is
silent in an online game. With WiFi on, NextZXOS starts in full each time.

### The Raspberry Pi

Some Spectrum Next machines have a Raspberry Pi Zero running NextPi, which some
programs use for music and other work. OverSpec can run the real NextPi behind its
Next, under QEMU.

You need QEMU (`qemu-system-arm`) and a folder holding NextPi's `kernel.img`, its
`.dtb` file and its card image (`.qcow2` or `.img`). OverSpec supplies neither.
Open More, Settings, NextZXOS, Pi and WiFi, set **Behind the Next** to NextPi, run
by QEMU, and choose the folder in **NextPi folder**. NextPi starts with the first
Next program you play, takes about a minute from cold, and stops when OverSpec
does. **Start NextPi now** and **Stop NextPi** are on the same page, which shows
when NextPi is ready. NextPi's card image is not changed. The Next hears NextPi's
sound when the Next program turns it on.

### The Developer view

Open Picture & sound, then Developer view, to look inside the Next's picture and
sound. Nothing in it changes the game or what is saved.

- Marks over the picture (they show in saved pictures too): where the Copper wrote a register (green), where the DMA
  moved a byte (red), where an interrupt was raised (magenta), and a box round each
  visible sprite (yellow).
- Layers left out: the ULA, Layer 2, the tilemap or sprites.
- Sound left out: the beeper, the DACs, or each sound chip.
- Pages in place of the picture: the palettes, the sprite patterns, the tile shapes
  and every NextREG.
- **Picture: whole display** in place of **Picture: 320 by 240**: the Next's whole
  640 × 256 picture, its full border and both halves of each pixel in Timex hi-res,
  Layer 2's 640-wide mode and 80-column tilemaps. It is fitted at 5:4.

## For programmers

### The debugger

Start a Spectrum or Next game and press F12. The game stops, and beside a smaller
picture you see its code, its registers (those that changed are highlighted), the
flags, the Next's memory pages, the stack, memory and the breakpoints.

Put the `.sld` file that sjasmplus writes with `--sld` beside your program with the
same name (`game.sld` for `game.nex`), and keep your source files where it says.
The debugger then shows your source. Where it cannot, it shows the disassembly, with
labels and source line numbers where it has them.

| Key | Does |
|---|---|
| F5 or C | Run until a breakpoint |
| S or Space | Step |
| N | Step over a call, a restart or a repeating instruction |
| O | Step out of the routine |
| P | Stop |
| B, or click the margin | A breakpoint on the marked line, or off again |
| Up, Down, Page Up, Page Down | Move the mark |
| Tab | Source or disassembly |
| M | Memory at HL, SP, IX, DE or PC |
| F12 or Escape | Close |

A breakpoint set in the disassembly keeps the memory page that was paged in there,
so a routine at the same address as another in a different page stops only for its
own. One set on a source line is set at every place that line was assembled, each
in its own page. (In the Next's ROM a breakpoint stops in any page.) Close the debugger with breakpoints set
and the game runs on; the debugger opens again when one is met. A pause you had on
before is back when it closes.

The debugger is not available in an online game or while a Next replay is being
recorded. A position cannot be saved while the debugger has stopped a game part way
through a frame.

### DeZog

Start OverSpec with `--debugger 11000` and DeZog in Visual Studio Code can attach
to a Spectrum or Next program. In DeZog's `launch.json`:

```json
"remoteType": "cspect",
"cspect": { "hostname": "localhost", "port": 11000 }
```

OverSpec listens on this computer only and takes one debugger at a time, DeZog or
its own. A break instruction in your program (FD 00, which sjasmplus's BREAK makes,
or DD 01 or ED FF) stops it while a debugger is attached.

### MCP server

Started with `--mcp`, OverSpec is an MCP server that an AI agent can drive, over its
standard input and output. For Claude Code:

```
claude mcp add overspec -- /path/to/overspec --mcp
```

The agent can load games, capture screenshots, press keys and run frames, and read
and change memory, registers, NextREGs, sprites, palettes and the Copper. It has the
same debugger as F12: source maps, breakpoints on `file.asm:120`, conditions such
as `b[score] > 10 && a != 0`, the call stack, and the source around the program
counter. The F12 window and the agent see each other's breakpoints.

### Tests without a screen

```
overspec --headless --data-dir FOLDER --scenario test.json
```

runs a list of steps with no display or sound, as fast as it can, and prints a line
of JSON for each step saying whether its answer was the one expected. The exit
status is 0 when every step passes, 1 when an answer differs, 2 when a step fails,
the run takes too long or ends before its steps are done, and 3 when the scenario
cannot be read or a step is not well formed. `--data-dir` must be given on the
command line. The format is in the README that comes with OverSpec.

### More for programmers

These are described in the README that comes with OverSpec:

- The Next's two serial ports, connected to a port on this computer
  (`tcp:PORT`), to a program that is listening (`connect:HOST:PORT`), or to a
  pseudo-terminal (`pty`, not on Windows): `--uart-esp`, `--uart-pi`,
  `--uart-joy-left`, `--uart-joy-right`.
- The Raspberry Pi's debug link, for a program of yours to stand in for the Pi:
  `--pi-spi tcp:PORT`, `--pi-spi-hz` (2 MHz unless given), the Pi's sound with
  `--pi-sound`, and `--nextpi-sound` to have NextPi send its sound that way.
- For Next programs: `--profile FILE` writes the time spent at each instruction
  address, and `--history FILE` the last 4,096 instructions with their registers,
  as OverSpec ends. `--exit-opcode` makes DD 00 end OverSpec with A as its exit
  status.
- `--nex-info FILE` prints what a `.nex` file's header holds.

## Options and the command line

`overspec GAME` starts a game. Most options can also be kept in a file, without the
dashes, one to a line:

```
[options]
sd-speed=slow
show=copper,sprites
window-size=1280 720
```

`overspec.ini` beside OverSpec is read for every game. For a game named on the
command line, `overspec.ini` in its folder and the game's own `.ini` beside it
(`beast.ini` for `beast.nex`) are read too. An option with no value is on by
itself or with `=1`, and off with `=0`. Later files win over earlier ones, and the
command line wins over them all. OverSpec prints the name of each file it reads and
any line it leaves out.

`--mcp`, `--scenario` and `--headless` work only on the command line. The files
beside a game may have come with it, so they cannot ask for anything that writes
files, opens the network or a port, runs a script, or lets a program end OverSpec.

| Option | Does |
|---|---|
| `--fullscreen` | Start full screen |
| `--quit-with-game` | Close OverSpec when the game is left, for front ends |
| `--library FOLDER` | The games folder |
| `--data-dir FOLDER` | Saves and settings in this folder, for this run |
| `--trdos ROM` | The TR-DOS ROM for Beta disk games |
| `--scale N` | Window size, 1 to 6 |
| `--window-size W H` | Window size in pixels, from 800 × 562 to 7680 × 4320 |
| `--theme FILE` | A `.theme` file for OverSpec's look |
| `--no-ident` | Skip the start-up ident |
| `--ident` | Show the ident where it would be skipped, if Start-up ident is on |
| `--host`, `--join CODE` | Play online |
| `--esp-wifi` | The Next's WiFi on |
| `--esp-wifi-local` | The Next's WiFi on, and allowed to reach this computer |
| `--sd-speed SPEED` | The Next's SD card speed: `slow`, `normal`, `fast`, `unlimited` or `READ,WRITE` |
| `--clock SECONDS` | Start the Next's clock at this many seconds of local time since 1970, for runs that must come out the same; `0` for no clock |
| `--show copper,dma,sprites,interrupts` | Developer view marks |
| `--hide ula,layer2,tilemap,sprites` | Developer view: layers left out |
| `--mute beeper,dacs,ay1,ay2,ay3` | Developer view: sound left out (`ay1a` and so on for one channel) |
| `--page N` | Developer view page: 1 palettes, 2 sprite patterns, 3 tile shapes, 4 NextREGs |
| `--native` | The whole display |
| `--debugger PORT` | DeZog's connection, port 1024 to 65535 |
| `--mcp` | Be an MCP server |
| `--headless`, `--scenario FILE` | Run without a screen; run a scenario |
| `--profile FILE`, `--history FILE`, `--exit-opcode`, `--nex-info FILE` | See [For programmers](#for-programmers) |
| `--uart-esp`, `--uart-pi`, `--uart-joy-left`, `--uart-joy-right` | The Next's serial ports |
| `--pi-spi`, `--pi-spi-hz`, `--pi-sound`, `--nextpi-sound` | The Raspberry Pi's link and sound |
| `--ui-script FILE`, `--ui-capture MS FILE` | Drive the interface from a script, or capture it after so many milliseconds and quit |
| `--help` | A short summary |

## Your files, updates and reports

Your saves, settings and pictures are kept in your data folder:

- Linux and macOS: `~/.local/share/overspec`
- Windows: `%APPDATA%\OverSpec`

On any system, `$XDG_DATA_HOME/overspec` is used instead where `XDG_DATA_HOME` is set.

Saved positions are in `saves/`, files a Next game writes in `files/`, NextZXOS's
card changes in `sd/` and saved pictures in `pictures/`.

To use another folder, open Player settings, Storage, browse to it and choose
**Use for saves and settings**. OverSpec uses it from the next start and does not
move what is already there: quit OverSpec, copy the old folder's contents across,
then start it again.
**Use for games** on the same page changes your games folder.

At most once a day, while it is open, OverSpec checks whether there is a newer
version. If there is, it offers **Update now** or **Open download page**, depending
on how it was installed, with **Later** and **Skip this version**. In Settings,
Updates, **New version alerts** turns the offer off and **Daily checks** stops the
checks.

**Report a problem** in Player settings lists what a report holds; choosing what
kind of problem it is sends it. A report from inside a game includes the game's file
name and a picture of the screen. After a crash or freeze, OverSpec asks at the next
start whether to send a report about it.
