
//Sucesion fibonacci

function fibonacci(n){
    resultado=[0,1]
    for(var i=2;i<=n;i++){
        var a=resultado[i-1]
        var b=resultado[i-2]
        resultado.push(a+b)

    }
    return resultado
}

console.log(fibonacci(10))
