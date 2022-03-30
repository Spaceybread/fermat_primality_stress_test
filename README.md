# fermat_primality_tstress
Puts a heavy load on the CPU by attempting to check if a number is prime or not; based on Fermat's Primality Test and inspired by GIMPS and Prime95

Open stress.py using command prompt and choose the number of instances you want to run, do not open mprime.py directly  

Do not start with more than 4 instances at first and gradually increase until your CPU is running at full capacity (on Windows, use task manager to check)

Do not leave this running for too long and do not attempt to open an insane amount of instances (My Ryzen 1700 could handle 16 instances so your mileage may vary)

Fermat's Primality Test uses Fermat's Little Theorem to check if a number is pseudoprime or composite (Read: https://en.wikipedia.org/wiki/Fermat_primality_test)

Prime95 is a similar program that is far more professional and contributes to GIMPS or the Great Internet Mersene Prime Search that you should check out if you find this interesting in any way!

I do not take responsiblity for any damage that you may sustain if you choose to run this script

Thanks! 
