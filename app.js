var somevariable = function(){console.log("Hi there !! Testing features of anonymous function")}

function firstfunction(greet){
  console.log(greet)
}

function mainfunction(somefunction, prm){
  somefunction(prm)
}

mainfunction(somevariable, "hello")
