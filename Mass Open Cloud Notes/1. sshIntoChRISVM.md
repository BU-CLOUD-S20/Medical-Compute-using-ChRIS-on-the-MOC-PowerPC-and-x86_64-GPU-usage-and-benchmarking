# Instructions for SSH-ing into ChRIS VM on OpenShift

Let's assume your private key is called cloud.key and your public key is called cloud.key.pub. 

1. Before SSH-ing, navigate to your **.ssh** folder and add your private key to the SSH cloud agent
```bash
$ cd ~/.ssh
$ ssh-add cloud.key
```

2. Then, if the public key was properly added to the VM's authorized key list, you can SSH into the ChRIS VM.
```bash
$ cd ~/.ssh
$ ssh ubuntu@128.31.25.45
```
