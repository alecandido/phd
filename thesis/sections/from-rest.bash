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
  sd '|(\w*?)|' '\\#$1\n' $input
  sed -e 's@\\#@\L\1@gi' -i $input
done

popd >/dev/null
