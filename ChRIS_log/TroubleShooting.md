
- Creating python3 virtual env on titan:
  ```
  mkvirtualenv --python=python3 test_new_env
  
  The path /home/chris-local/kefan/iso/python3 (from --python=python3) does not exist
  ```
  
  Problem: path mentioned in tutorial couldn't be found
  
  Solution: give specific path
  ```
  mkvirtualenv --python=python3 test_new_env
  
  (test_new_env) [chris-local@titan:x86_64-Linux]...local/kefan/iso$>
  ```
 - Step 3 in cookiecutter tutorial:
    ```
    cookiecutter https://github.com/FNNDSC/cookiecutter-chrisapp.git
    ```
    and get result asking for username and passwd, then get error like:
    ```
      Traceback (most recent call last):
      File "/home/chris-local/python_envs/app_env/bin/cookiecutter", line 8, in <module>
        sys.exit(main())
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/click/core.py", line 829, in __call__
        return self.main(*args, **kwargs)
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/click/core.py", line 782, in main
        rv = self.invoke(ctx)
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/click/core.py", line 1066, in invoke
        return ctx.invoke(self.callback, **ctx.params)
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/click/core.py", line 610, in invoke
        return callback(*args, **kwargs)
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/cookiecutter/cli.py", line 121, in main
        password=os.environ.get('COOKIECUTTER_REPO_PASSWORD')
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/cookiecutter/main.py", line 63, in cookiecutter
        password=password
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/cookiecutter/repository.py", line 103, in determine_repo_dir
        no_input=no_input,
      File "/home/chris-local/python_envs/app_env/lib/python3.7/site-packages/cookiecutter/vcs.py", line 99, in clone
        stderr=subprocess.STDOUT,
      File "/usr/lib/python3.7/subprocess.py", line 411, in check_output
        **kwargs).stdout
      File "/usr/lib/python3.7/subprocess.py", line 512, in run
        output=stdout, stderr=stderr)
    subprocess.CalledProcessError: Command '['git', 'clone', 'https://github.com/FNNDSC/matrixbench.git']' returned non-zero exit status 128.
      ```

    Solution: don't change the original command to create new plugin
    
- Command mkvirtualenv not found after installing virtualenvwrapper
  
  Solution:
  ```
  source `which virtualenvwrapper.sh`
  ```
  before use mkvirtualenv
  
 - Creating a parent folder during making ChRIS app with cookiecutter:
 
  Solution:
  
  make sure switch to the child folder after this command:
  ```
  cookiecutter https://github.com/FNNDSC/cookiecutter-chrisapp.git
  ```
  is finished
  
 - Docker container on Titan can't access to Internet: not fixed, also using dockerhub build takes 15-20 mins per build
 
    Temporary Solution:
  - download nvidia/cuda to local machine
  - Modify Python script and **docker build** on local machine (Mac)
    ```
    docker build .
    ```
  - Push to **Dockerhub**
    ```
    docker tag a4c7436229d5 robertmorrislike/mat-test
    docker push robertmorrislike/mat-test
    ```
  - docker pull on Titan
    ```
    docker pull robertmorrislike/mat-test
    ```
  - docker run on Titan
    ```
    docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=1 robertmorrislike/mat-test python3 matmultiply.py -c 32,32,128 in out
    ```
    
    # ITS RUNNING !!! GOOOOOOOOOOD!!!!!
    
    Command:
    ```
    docker pull fnndsc/pl-matmultiply
    mkdir in out && chmod 777 out
    docker run --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=1 -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing fnndsc/pl-matmultiply python3 matmultiply.py -c 32,32,128 /incoming /outgoing

    ```
