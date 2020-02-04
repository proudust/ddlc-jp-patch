result=0
`dirname $0`/dependencies.sh || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

echo "Extract dialogs Doki Doki Literature Club! v1.1.1"
/tmp/renpy/renpy.sh /tmp/ddlc dialogue --strings --escape
sed "s|`pwd`|game|" /tmp/ddlc/dialogue.tab >./dialogue.tab
