// Solution to https://projecteuler.net/problem=1
console.log(
    Array.apply(null,{length : 999})
        .map((v,i)=>(i+1))
            .filter(v=>(v%3 == 0) || (v%5 == 0))
                .reduce((sum, v) => sum += v))
