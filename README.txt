
VARIABLEN

int x = 10
bool x = true
str x = "hi"



FUNKTIONEN

str test<int a, int b> {
    
}


FALLUNTERSCHEIDUNG


? <test == "hallo"> {
    test = "hi"

} ? <test == "tschüss"> {
    test = "bye"

} ? <> {
    test = "dont know"
}




BUILDIN

casting

print <test>        OUTPUT
read <"input: ">    INPUT






<ERROR> 
-> page not found




str readFile<str file> {
    ? <read> {
        ret file
    } ? <> throw "no permissions"
}

try{
    str content = readFile<"test.txt">
} catch {
    
}

Error handling?
