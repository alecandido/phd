INPUTS=$@
FOLDER=$(dirname $1)
CHAPTER=$(basename $FOLDER)
echo "Importing files for chapter '$CHAPTER'"
echo

pushd $FOLDER >/dev/null

for texinput in $@; do
  echo "- $texinput"
  input=$(basename $texinput)

  rg newcommand -- $input
  if [ $? == 0 ]; then
    continue
  fi

  sd -p '(\\label\{.*):' '$1/dis:' $input

  echo "finished processing $texinput"
done

popd >/dev/null
