# Run the simulator 100 times and rename the output.
for (($i = 0); $i -lt 100; $i++)
{
    gradle :simulator:run
    Rename-Item -Path "C:\Users\berna\Documents\GitHub\simblock\simulator\src\dist\output\chainlength.json" -NewName "C:\Users\berna\Documents\GitHub\simblock\simulator\src\dist\output\chainlengthbest$i.txt"
}

