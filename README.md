# A simple RSA Encryption algorithm implementation

To Run
------
Optionally one can generate a list of prime numbers, by.

```
    USER:~/.../rsa-example/src
    λ python prime_gen.py --help
    [out] 
        usage: prime_gen.py [-h] L

        Generation of prime numbers

        positional arguments:
          L           Provide the Limit

        optional arguments:
          -h, --help  show this help message and exit
    
    USER:~/.../rsa-example/src
    λ python prime_gen.py 100
    [out]
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

```

From there, one can choose any two(three) prime numbers.

Let P = 73, Q = 89 and take e = 17

We run **rsa_keygen.py**

```
    USER:~/.../rsa-example/src
    λ python rsa_keygen.py --help
    [out]
        usage: rsa_keygen.py [-h] [-e KEY] P Q

        Simple RSA key generator.

        positional arguments:
          P                  The prime value of P.
          Q                  The prime value of Q.

        optional arguments:
          -h, --help         show this help message and exit
          -e KEY, --key KEY  The co-prime value of e.
          
    USER:~/.../rsa-example/src
    λ python rsa_keygen.py 73 89 -e 17
    [out]

            Generated Keys!
            Phi N               : 6336
            Public  Key, (N, e) : (6497, 17)
            Private Key, d      : 2609
```

Now, let us run **rsa.py**

```
    USER:~/.../rsa-example/src
    λ python rsa.py --help
    [out]
        usage: rsa.py [-h] [-e] [-d] -k KEY -m MESSAGE N

        Simple RSA Encryption Algorithm.

        positional arguments:
          N                     The RSA modulo value, N.

        optional arguments:
          -h, --help            show this help message and exit
          -e, --encrypt         If true the provided message will be encrypted.
          -d, --decrypt         If true the provided message will be encrypted.
          -k KEY, --key KEY     The encryption e or decryption key d
          -m MESSAGE, --message MESSAGE
                                The message to be encrypted or the cipher to be decrypted.
                    
    USER:~/.../rsa-example/src
    λ python rsa.py 6497 -e -k 17 -m "Hello, RSA from Github"
    [out]
        2116-5708-4259-4259-4939-5486-5418-3715-4244-3148-5418-5099-3196-4939-71-5418-2591-1695-928-569-4318-3685

    USER:~/.../rsa-example/src
    λ python rsa.py 6497  -d -k 2609 -m\        
            "2116-5708-4259-4259-4939-5486-5418-3715-4244-3148-5418-5099-3196-4939-71-5418-2591-1695-928-569-4318-3685"
    [out]
        Hello, RSA from Github
```

That is more like it...
-----------------------
