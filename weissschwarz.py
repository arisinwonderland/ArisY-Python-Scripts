import os
import re
        
input_path = "data"
output_path = "traits.csv"

files = os.listdir(input_path)

sets = {}

for file in files:
    if file.endswith(".txt"):
        file_path = os.path.join(input_path, file)

        with open(file_path, "r", encoding="utf-8-sig") as f:
            try:
                l = ""
                for i in range(0,10):
                    l = f.readline()
                    m = re.match(r"Character:? (\w+\/\w+)-", l)
                    if m:
                        break

                if m:
                    set_name = m.group(1)
                    sets[file] = [set_name, set()]
                    
                    for line in f:
                        m = re.match(r"Trait\d (.+)", line)
                        if m:
                            val = m.group(1).replace('"','""')
                            if re.search(",", val):
                                val = '"' + val + '"'
                            sets[file][1].add(val)
                else:
                    print('Match failed for filename "%s"'%(file))
            except UnicodeDecodeError:
                print('Decoding failed for filename "%s"'%(file))
                continue
            
with open(output_path, mode="w") as file:
    for key, value in sets.items():
        line = "{filename},{setname},{traits}\n".format(filename=key, setname=value[0], traits=",".join(value[1]))
        file.write(line)
