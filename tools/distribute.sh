PATCH_VERSION=$(git -C $(dirname $0)/.. describe --tags)

result=0
`dirname $0`/dependencies.sh || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

echo "Build Doki Doki Literature Club! JP patch ver$PATCH_VERSION for v1.1.1"
rm -rf /tmp/ddlc-jp
cp -fpr /tmp/ddlc /tmp/ddlc-jp
cp -fpr `dirname $0`/../* /tmp/ddlc-jp

result=0
/tmp/renpy/renpy.sh /tmp/renpy/launcher distribute /tmp/ddlc-jp --package Mod || result=$?
if [ ! "$result" = "0" ]; then
  exit 1
fi

rm -rf /tmp/ddlc-jp-dist ./DDLC_JP_$PATCH_VERSION ./DDLC_JP_$PATCH_VERSION.zip
unzip -q `ls /tmp/*-dists/*-Mod.zip` -d /tmp/ddlc-jp-dist
mv `ls -d /tmp/ddlc-jp-dist/* | head -n1` ./DDLC_JP_$PATCH_VERSION
zip -q -r ./DDLC_JP_$PATCH_VERSION.zip ./DDLC_JP_$PATCH_VERSION
