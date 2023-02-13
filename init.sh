SIP_PATH=`pwd`
SIP_PATH='export SIP_PATH="'"$SIP_PATH"'"'
PYTHON3=`which python3`
SIP='alias sip="PYTHONPATH=$SIP_PATH '"$PYTHON3"' $SIP_PATH/sip/sip.py"'

echo $SIP_PATH >> ~/.bash_profile
echo $SIP >> ~/.bash_profile
source ~/.bash_profile
