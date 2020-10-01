# Maplestory Packet Puller

## Features:
 - Reads keywords from IDA-generated pseudocode, and formats them into a form that is friendly for server encodes
 - Options for varying the accuracy of packet structure pulls
 - Shows the structure of packets
 - Writes all packet structures to an identically named output file in `MaplePacketPuller/IDA Maple Script/FuncOutput/`
 
## Known Issues:
  - Edge-case functions may cause errors; see comments in the source code for possible fixes, i.e. line 159
  - `while()` loops aren't properly handled, i.e. whether a decode is in the scope of one well
    - Possible circumvention: may be rectified if `GET_ALL_DECODES = true`
  - The constant `GET_ALL_DECODES` when set to `True` for increased accuracy, has major aesthetic drawbacks
  - This script assumes that you have named the disassembled function in IDA according to the function you want to pull packet structures from
  - This script does not display switch cases - can be added by user

## Technical Stack
|  | Target | Tested |
| --- | --- | --- |
| Python | 3.8.6 | 3.8.6 |
| IDA Pro 32-bit | 7.0 | 7.0 |
| Editor | Atom | Atom |
| CLI Interpretor | cmd | pwsh 7.0 |

Other variants for contributors to test:
  - [ ] Python 2.7
  - [ ] Python 3.6
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
 
1. Navigate to `MaplePacketPuller/IDA Maple Script/` in CLI and run `Analysis.py`
    - Alternatively use a Python IDE like PyCharm
 
2. Input the name of the file you want to analyze, i.e. the txt file you've just created
 
3. Let the program analyze it.
 
4. Now packet structure should be yours! :octocat:
    - see `MaplePacketPuller/IDA Maple Script/FuncOutput/`

 The console output should look a little something like this:
 
 ![OnSetField](https://media.discordapp.net/attachments/746519006961336370/755117561024086036/061591b5c3d0f4a3247f9367b91b9843.png)
