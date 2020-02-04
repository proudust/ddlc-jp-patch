if [ ! -f /tmp/renpy/renpy.sh ]; then
  echo "Download Ren'Py SDK v6.99.12.4"
  wget -q -O /tmp/renpy.tar.bz2 https://www.renpy.org/dl/6.99.12.4/renpy-6.99.12.4-sdk.tar.bz2
  tar -xf /tmp/renpy.tar.bz2 -C /tmp
  rm /tmp/renpy.tar.bz2
  mv /tmp/renpy-6.99.12.4-sdk /tmp/renpy

  echo "Apply Extract Dialogue patch to Ren'Py"
  wget -q -O /tmp/renpy/renpy/translation/dialogue.py https://raw.githubusercontent.com/proudust/renpy/dialogue-patch/renpy/translation/dialogue.py
fi

if [ ! -d /tmp/ddlc ]; then
  echo "Download Doki Doki Literature Club! v1.1.1"
  wget -qO /tmp/ddlc.zip `curl -qsX POST https://teamsalvato.itch.io/ddlc/file/594897 | jq -r .url`
  unzip -q /tmp/ddlc.zip -d /tmp
  rm /tmp/ddlc.zip
  mv /tmp/DDLC-1.1.1-pc/ /tmp/ddlc/

  if [ ! -f /tmp/rpatool/rpatool ]; then
    echo "Download rpatool"
    git clone https://github.com/Shizmob/rpatool.git /tmp/rpatool >/dev/null
  fi

  echo "Unpacking Doki Doki Literature Club! v1.1.1"
  python2 /tmp/rpatool/rpatool -x /tmp/ddlc/game/scripts.rpa -o /tmp/ddlc/game

  if [ ! -f /tmp/unrpyc/unrpyc.py ]; then
    echo "Download unrpyc"
    git clone https://github.com/CensoredUsername/unrpyc.git /tmp/unrpyc >/dev/null
  fi

  echo "Decompile Doki Doki Literature Club! v1.1.1"
  python2 /tmp/unrpyc/unrpyc.py /tmp/ddlc/game/*.rpyc
fi
