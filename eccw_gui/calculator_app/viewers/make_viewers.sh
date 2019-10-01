#! /bin/bash

# Makes py-qt based python viewers from xml files (.ui) generated by Qt-designer.

inpath=../uis
for filename in $inpath/*.ui; do
    in=$filename
    out=${filename/uis/viewers}
    out=${out::-3}.py
    pyuic5 -x $in -o $out
    # Fix ressource import path
    sed -i -e 's/import ressources_rc/import eccw_gui.images.ressources_rc/g' ./$out
done

