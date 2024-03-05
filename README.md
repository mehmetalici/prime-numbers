# prime-numbers
The program finds 100 prime numbers after a given number.

## Getting started
Step-by-step instructions to run the program:
### Prerequisites
- Python 3

### Installing
1. Clone the project:
    ```bash
    git clone git@github.com:mehmetalici/prime-numbers.git
    ```
2. Run the program by passing the number after which 100 prime numbers shall be printed. For example, to print 100 prime numbers after 3000, run the program as follows:
    ```bash
    cd prime-numbers
    python prime_numbers.py 3000
    ```

## Complexity Analysis
The algorithm is comprised of two functions: `is_prime` and `find_primes`. `is_prime` iterates from 2 to the square root of the number and therefore it is $O(\sqrt n)$. Moreover, `find_primes` loops over $m$ times and uses `is_prime` at each iteration. Therefore, its complexity is $O(\sqrt n*m)$. 

If $m$ is kept constant, which is 100 in this program, the complexity of the algorithm can be reduced to $O(\sqrt n)$.   

