# Maplestory Packet Puller

## Features:
 - Reads keywords from IDA-generated pseudocode, and formats them into a form that is friendly for server encodes
 - Options for varying the accuracy of packet structure pulls
 - Shows the structure of packets
 - Writes all packet structures to an identically named output file in `MaplePacketPuller/IDA Maple Script/FuncOutput/`
 - Ability to search for InHeader opcodes
 
## Known Issues:
  - `while()` loops aren't properly handled, i.e. whether a decode is in the scope of one well
    - Possible circumvention: may be rectified if `GET_ALL_DECODES = true`
  - The constant `GET_ALL_DECODES` when set to `True` for increased accuracy, has major aesthetic drawbacks
  - This script assumes that you have named the disassembled function in IDA according to the function you want to pull packet structures from
  - This script does not display switch cases - can be added by user

## Technical Stack
|  | Target | Tested |
| --- | --- | --- |
| Python | 3.8.5 | 3.6.12 & 3.8.6 |
| IDA Pro 32-bit | 7.0 | 7.0 |
| Editor | Atom | Atom |
| CLI Interpretor | cmd | pwsh 7.0 |

Other variants for contributors to test:
  - [x] Python 2.7
    - **NOT COMPATIBLE:** use of os.scandir() makes it non-backwards compatible with versions older than 3.6
  - [x] Python 3.6
    - <del>**NOT COMPATIBLE:** probably a result of how f-strings handle backslashes</del>
    - *Update: Fixed as of commit 10a9fd86c4da264ef6d1d73a6aca248343cf63f6*
  - [ ] IDA 6.8
  - [ ] IDA 7.5
  - [ ] IDLE
  - [ ] PyCharm Community Edition 2020.1.1 (or later)

---
# How to use

**INPUT:**  `.txt` file containing C-pseudocode from IDA disassembly

**OUTPUT:**  `.txt` file containing packet structure & console output


- NOTE: You will have to create a `.txt` file in the `Functions` directory with the copy-pasted pseudocode from IDA (examples in there)
  - `MaplePacketPuller/IDA Maple Script/Functions`

1. Navigate to `MaplePacketPuller/IDA Maple Script/src/main/python` in `CLI` and run `main.py`
    - Alternatively use a Python IDE like PyCharm

2. Input the type of Analysis you want to do

3. Input the name of the file you want to analyze, i.e. the txt file you've just created
 
4. Let the program analyze it.
 
5. Now packet structure should be yours! :octocat:
    - see `MaplePacketPuller/IDA Maple Script/FuncOutput/`

 The console output should look a little something like this:
 
 ![OnSetField](https://media.discordapp.net/attachments/746519006961336370/755117561024086036/061591b5c3d0f4a3247f9367b91b9843.png)
 ![InHeader](https://cdn.discordapp.com/attachments/631249406775132182/761270430823612476/a1e9fd7703d4ba359d314027a47c7b3b.png)
