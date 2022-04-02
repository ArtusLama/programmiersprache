
VARIABLEN

int x = 10
bool x = true
str x = "hi"



FUNKTIONEN

str test<int a, int b> {
    
}


FALLUNTERSCHEIDUNG


if <test == "hallo"> {
    test = "hi"

} <test == "tschüss"> {
    test = "bye"

} <> {
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
        return file
    } ? <> throw "no permissions"
}

try{



    str content = readFile<"test.txt">
} catch {
    
}

Error handling?
...



# THIS IS A COMMENT

GRAMMAAAAARRRRR


print <"Hello World">   (PRINT | LESS | STRING/VARIABLE | GREATER)
int x = 10              (VAR_TYPE | VAR_NAME | EAQUALS | TYPE)
                            |--------- same types ---------|
