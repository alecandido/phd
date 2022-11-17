INPUTS=$@
FOLDER=$(dirname $1)
CHAPTER=$(basename $FOLDER)
echo "Importing files for chapter '$CHAPTER'"
echo

pushd $FOLDER >/dev/null
for texinput in $@; do
  echo "- $texinput"
  input=$(basename $texinput)

  # convert rest abbreviations to macros
  sd '\|(\w*?)\|' '\\#$1\n' $input
  sed -e 's@\\#\(.*\)@\\\L\1@g' -i $input

  # translate inline math
  sd ':math:`(.*?)`' '$ $1$' $input
  sd '\$ ' '$' $input

  echo "finished processing $texinput"
done

popd >/dev/null
