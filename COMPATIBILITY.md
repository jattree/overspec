# What has been tested

OverSpec 0.6.20261117 was run against every file in the 2012 TOSEC Spectrum set: 42,427 tapes, disks and snapshots. 40,653 of them (95.8%) match the reference emulator, and another 939 run on where the reference stops or falls behind. The run was made on 2026-11-15; these pages are generated from its records.

## What the words mean

- **Good**: it loads, and its picture matches a reference emulator (Fuse).
- **Ahead**: it loads and runs on, while the reference emulator stops or falls behind, so the pictures cannot be matched. Usually a tape the reference does not start or finish by itself.
- **Runs**: it loads and runs, and there was no reference picture to compare with.
- **Check**: it runs, but part of the picture differs from the reference, or the reference gets further in the same time. Often a different moment in a title sequence or a slower tape load.
- **Differs**: it runs, but most of the picture differs from the reference. These need a look.
- **Fails**: it does not load.
- **Save and restore**: a save taken part way and loaded again gives exactly the same picture, sound and state.

## How it was measured, and what that does not show

Each file was started with nobody at the controls and its picture compared with Fuse's after about a minute. Where that one picture did not match, both emulators were run for three minutes and every picture from one compared with every picture from the other, to tell a real difference from the same thing happening at a different moment.

This does not show that a game can be played to the end, or that it sounds right. A program waiting for a key counts as Good if both emulators wait at the same screen. Only about a hundred of the mismatches have been looked at by a person, so some Check and Differs entries will turn out fine and some Good ones will not. If a game you care about misbehaves, an [issue](https://github.com/jattree/overspec/issues) is welcome.

## Summary

| | Tested | Good | Ahead | Runs | Check | Differs | Fails |
|---|---|---|---|---|---|---|---|
| All files | 42427 | 40653 | 939 | 2 | 606 | 225 | 2 |

### By category

| | Tested | Good | Ahead | Runs | Check | Differs | Fails |
|---|---|---|---|---|---|---|---|
| Games | 29808 | 28653 | 642 | 0 | 362 | 149 | 2 |
| Applications | 4155 | 4073 | 56 | 0 | 23 | 3 | 0 |
| Covertapes | 2635 | 2442 | 86 | 2 | 82 | 23 | 0 |
| Magazines | 2536 | 2383 | 70 | 0 | 50 | 33 | 0 |
| Compilations | 1827 | 1729 | 54 | 0 | 37 | 7 | 0 |
| Demos | 1107 | 1024 | 22 | 0 | 51 | 10 | 0 |
| Educational | 350 | 341 | 9 | 0 | 0 | 0 | 0 |
| Documentation | 9 | 8 | 0 | 0 | 1 | 0 | 0 |

### By file format

| | Tested | Good | Ahead | Runs | Check | Differs | Fails |
|---|---|---|---|---|---|---|---|
| tzx | 18727 | 17627 | 579 | 2 | 375 | 144 | 0 |
| z80 | 12358 | 12324 | 2 | 0 | 17 | 13 | 2 |
| tap | 7160 | 6790 | 250 | 0 | 88 | 32 | 0 |
| trd | 1518 | 1373 | 32 | 0 | 91 | 22 | 0 |
| dsk | 1283 | 1201 | 67 | 0 | 8 | 7 | 0 |
| scl | 1040 | 1002 | 9 | 0 | 25 | 4 | 0 |
| sp | 257 | 257 | 0 | 0 | 0 | 0 | 0 |
| slt | 69 | 66 | 0 | 0 | 2 | 1 | 0 |
| csw | 15 | 13 | 0 | 0 | 0 | 2 | 0 |

## The lists

Every file, by TOSEC category and then by title. The whole list is also one file, [tosec.csv](compatibility/tosec.csv), with each file's SHA-256.

- [Everything marked Differs or Fails](compatibility/needs-a-look.md)
- **Games:** [007 - A View to a Kill to Alchemist](compatibility/games-01.md), [Alchemist to Badlands](compatibility/games-02.md), [Badlands to Bounty Bob Strikes Back](compatibility/games-03.md), [Bounty Bob Strikes Back to Cluedo](compatibility/games-04.md), [Cluedo to Death Valley - Motion on Dea](compatibility/games-05.md), [Death Wake to Echelon](compatibility/games-06.md), [Echelon to Four Great Games Volume 1 -](compatibility/games-07.md), [Four Great Games Volume 1 - to Gremlins - The Adventure](compatibility/games-08.md), [Gremlins - The Adventure to Imagination](compatibility/games-09.md), [Imagination to Kirel](compatibility/games-10.md), [Klad to Man-Trap](compatibility/games-11.md), [Manager to Munchman](compatibility/games-12.md), [Munchman to Para Assault Course](compatibility/games-13.md), [Parabola to Questprobe 3 - The Human Tor](compatibility/games-14.md), [Questprobe 3 - The Human Tor to Saboteur](compatibility/games-15.md), [Saboteur to Soho Sex Quest](compatibility/games-16.md), [Soho Sex Quest to Summer Santa](compatibility/games-17.md), [Summer Santa to Top Cat in Beverly Hills Cat](compatibility/games-18.md), [Top Cat in Beverly Hills Cat to Wells & Fargo](compatibility/games-19.md), [Wells & Fargo to Zzzz](compatibility/games-20.md)
- **Applications:** [+3 Utilities to Graf 3](compatibility/applications-01.md), [Graf 3 to RS 232C Interface](compatibility/applications-02.md), [RS 232C Interface to ZZZ-UNK-TLWORD](compatibility/applications-03.md)
- **Covertapes:** [15 puzzle to Octipede](compatibility/covertapes-01.md), [Oink! - Piggy Tales to ZX-Word, The](compatibility/covertapes-02.md)
- **Magazines:** [#z80 01 to Polesse 05](compatibility/magazines-01.md), [Polesse 06 to ZX-Power 04](compatibility/magazines-02.md)
- **Compilations:** [#z80 01-05 to Spy vs Spy Trilogy - Spy vs](compatibility/compilations-01.md), [Stack Light Rifle - Grouse S to ZxZvm - Scott Adams Adventur](compatibility/compilations-02.md)
- **Demos:** [128 Demo to ZZZ-UNK-SamGraphicsDemo](compatibility/demos-01.md)
- **Educational:** [Acids, Bases and Salts to What's the Time - Quarter Ho](compatibility/educational-01.md)
- **Documentation:** [48 Irons - Help to Virus - Help](compatibility/documentation-01.md)

## Played by a person

| Game | System | Date | Result |
|---|---|---|---|
| Alien 8 (1985)(Ultimate Play The Game) | Windows 11 | 2026-11-11 | Played. No problems reported. |

## Other kinds

TOSEC does not hold these. They come from an earlier run over a smaller collection; there is no reference emulator for them, so the picture is not compared.

| Kind | Tested | Good | Runs | Check | Differs | Fails |
|---|---|---|---|---|---|---|
| Spec256 and ZX-Poly colour editions | 52 | 0 | 52 | 0 | 0 | 0 |
| NexClash .nxc patches | 54 | 0 | 54 | 0 | 0 | 0 |
| Native Spectrum Next | 26 | 0 | 26 | 0 | 0 | 0 |

### Spec256 and ZX-Poly colour editions

| Title | Format | Result | Save and restore | Detail |
|---|---|---|---|---|
| Abu Simbel Profanation | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Abu Simbel Profanation (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Alien 8 (ZX-Poly) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Army Moves (Part 1) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Army Moves (Part 1) (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Army Moves (Part 2) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Army Moves (Part 2) (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Atic Atac | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Atom Ant | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Booty | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Bruce Lee | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Bubbler | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Chuckie Egg | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Comando Quatro (ZX-Poly) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cybernoid | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cybernoid II | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy - The Ultimate Cartoon Adventure | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Everyone's a Wally | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Exolon | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Flying Shark (ZX-Poly) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Game Over (Part 1) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Game Over (Part 1) (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Game Over (Part 2) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Game Over (Part 2) (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Green Beret (auto colour v37) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Gun Runner | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Head over Heels | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Highway Encounter | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Into the Eagle's Nest | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Jetpac | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Jilly's Farm Vol. 1 - SokoBAArn | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Knight Lore | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Lode Runner | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Mad Mix 2 - En el Castillo de los Fantasmas | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Mad Mix 2 - En el Castillo de los Fantasmas (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Movie | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Official Father Christmas (ZX-Poly) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Pac-Mania | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Page and the Curse of the Pharaoh | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Phantis (Part 1) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Phantis (Part 1) (English) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Renegade | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Ruff and Reddy | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Sabre Wulf | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Scooby-Doo | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Silkworm | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Solomon's Key | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Summer Santa 2022 Update (ZX-Poly) | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| That Sinking Feeling | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Three Weeks in Paradise | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Treasure Island Dizzy | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Underwurlde | 256 | Runs | Exact | Runs. No reference emulator to compare the picture with |

### NexClash .nxc patches

| Title | Format | Result | Save and restore | Detail |
|---|---|---|---|---|
| Abu Simbel Profanation (1985)(Dinamic)(ES)[a][a] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Alien 8 (1985)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Army Moves (1987)(Imagine)(128K)[re-release] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Atic Atac (1983)(Ultimate Play The Game)[a8][a8] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Beyond the Ice Palace (1988)(Elite Systems)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Bubbler (1987)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cauldron (1985)(Palace) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Chase H.Q. (1989)(Ocean)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Chuckie Egg (1983)(A'n'F)[a3][a3] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cobra (1986)(Ocean) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Commando (1985)(Elite Systems)[aka Space Invasion] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cybernoid - The Fighting Machine (1988)(Hewson Consultants)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cybernoid II - The Revenge (1988)(Hewson Consultants)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Cyclone (1985)(Vortex)[a][a] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy - The Ultimate Cartoon Adventure (1987)(Code Masters) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy 2 - Treasure Island Dizzy (1989)(Code Masters)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy 3 - Fantasy World Dizzy (1989)(Code Masters)(128K)[a2][a2] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy 4 - Magicland Dizzy (1990)(Code Masters)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dizzy 6 - Dizzy, Prince of the YolkFolk (1991)(Code Masters)(128K)[a][a][aka Dizzy VI - Prince of the Yolkfolk] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Dynamite Dan (1985)(Mirrorsoft) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Everyone's a Wally (1985)(Mikro-Gen) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Game Over (1987)(Imagine)(128K)[re-release] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Ghosts 'n Goblins (1986)(Elite Systems)[aka Ghost 'n Goblins] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Green Beret (1986)(Imagine)[a2][a2] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Gryzor (1987)(Ocean)(48K-128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Gunfright (1985)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Herbert's Dummy Run (1985)(Mikro-Gen) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Ikari Warriors (1988)(Elite Systems)(48K-128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Incredible Shrinking Fireman, The (1986)(Mastertronic) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Jet Pac (1983)(Ultimate Play The Game)(16K)[a2][a2] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with. OverSpec runs this on 48K; strict 16K hardware is not implemented |
| Knight Lore (1984)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Knight Tyme (1986)(Mastertronic Added Dimension)(128K)[Magic Knight 3] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Lode Runner (1984)(Software Projects)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Lunar Jetman (1983)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Martianoids (1987)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Match Day (1984)(Ocean) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Midnight Resistance (1990)(Ocean)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| New Zealand Story, The (1989)(Ocean)(48K-128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Nightshade (1985)(Ultimate Play The Game)[a][a] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Nodes of Yesod (1985)(Odin Computer Graphics)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Pac-Mania (1988)(Grandslam)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Pyjamarama (1984)(Mikro-Gen) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Quazatron (1986)(Hewson Consultants)[aka Ziggurat] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Rainbow Islands - The Story of Bubble Bobble 2 (1990)(Ocean)(128K)[a][a] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Rambo - First Blood Part II (1985)(Ocean) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Renegade (1987)(Imagine)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Sabre Wulf (1984)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Smash TV (1991)(Ocean)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Solomon's Key (1987)(U.S. Gold) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Spellbound (1985)(Mastertronic Added Dimension)(128K)[Magic Knight 2] | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Starquake (1985)(Bubble Bus) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Target - Renegade (1988)(Imagine)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Three Weeks in Paradise (1986)(Mikro-Gen)(128K) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Underwurlde (1984)(Ultimate Play The Game) | nxc | Runs | Exact | Runs. No reference emulator to compare the picture with |

### Native Spectrum Next

| Title | Format | Result | Save and restore | Detail |
|---|---|---|---|---|
| 1MBTEST | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| 2MBTEST | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| ATICATAC | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| bbcbasic | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Bloaters | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| BombJack | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Daybreak | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| hott | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| lom | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| main | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| NextDAWDemo | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| NEXTEST | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| nextoid | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| NextSIDplayer | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Night-Knight-Demo | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| nxmodplayer | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| NXtel | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| plotit-lite | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| RevivalSurvival | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| SantasPressie | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| ScrollNutter | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| show512 | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Spectron2084 | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| TileEditor | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| tm | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |
| Warhawk | nex | Runs | Exact | Runs. No reference emulator to compare the picture with |

