# Instructions to get access to the ChRIS VM that's on OpenShift

For reference, [Link to MOC SSHing instructions](https://github.com/CCI-MOC/moc-public/wiki/SSH-to-Cloud-VM).

Please note that these instructions assume the ChRIS VM has already been created on OpenShift and therefore, you just need to share your public key with the person who instantiated the VM. 

1. Create a key pair 
    
  ```bash
    $ cd ~/.ssh
    $ ssh-keygen -t rsa -f ~/.ssh/cloud.key -C "label_your_key" 
  ```
  
2. Note the two keys that are created in your .ssh folder.

 ```bash
   cloud.key      # private key - don’t share this with anyone, and never upload it anywhere ever
   cloud.key.pub  # this is your public key    
 ```
 
3. Now, share your public key with the person who instantiated the ChRIS VM. In this case, that is Lizzy.

4. Then, Lizzy will add your public key to a text file and secure copy it into the VM.

 ```bash
   scp teammates.pub ubuntu@129.10.3.66:~
 ```
 
5. Then, Lizzy will append your public key onto the list of authorized keys.

 ```bash
   cat testfile >> ~/.ssh/authorized_keys
 ```
