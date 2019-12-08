Assignment 4 | IHM2016501 | Pradeep Gangwar

# How to run

    In the root directory of the folder run `python3 main.py` to execute the program. This will make 4 files (explained below).
    All 4 files contains the 1000 numbers generted from different methods.

    To obtain the chi square value for each method you need to run `python3 chi_square.py <file-name.txt>`. Replace the filename
    by the name of file which contains the random numbers of that method.

# Values of variables choosen

    Seed value for all the methods : 0.342

    Additive CG: a = 2.96, c = 0.25, m = 1.0
    Multiplicative CG: a = 2.96, c = 0.25, m = 1.0
    Mixed CG: a = 2.96, c = 0.25, m = 1.0


# Project Structure

    - main.py
    - additive_lcg.txt
    - multiplicative_lcg.txt
    - mixed_lcg.txt
    - default_generator.txt
    - Report.pdf
    - README.txt

    main.py: THis file contains the main code of the project.

    additive_lcg.txt: This file contains the 1000 random numbers generated using additive congruence generator.

    multiplicative_lcg.txt: This file contains the 1000 random numbers generated using multiplicative congruence generator.

    mixed_lcg.txt: This file contains the 1000 random numbers generated using mixed/linear congruence generator.

    default_generator.txt: This contains the 1000 numbers generated using the python's inbuilt random class.