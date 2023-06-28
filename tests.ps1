# Run the simulator 30 times and rename the output.
for (($i = 0); $i -lt 30; $i++)
{
    gradle clean build 
    gradle :simulator:run
    Rename-Item -Path "C:\Users\berna\Documents\GitHub\simblock\simulator\src\dist\output\graph\chainlength.json" -NewName "C:\Users\berna\Documents\GitHub\simblock\simulator\src\dist\output\graph\chainlengthbest$i.txt"
}

