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

  # scope all labels and references
  sd '(\\label\{.*?):' '$1/'$CHAPTER':' $input
  sd '(\\.?ref\{.*?):' '$1/'$CHAPTER':' $input
  # revert accidental multiple applications of scope
  sd '(\\.*?(ref|label)\{.*?)(/dis)*:' '$1/'$CHAPTER':' $input

  echo "finished processing $texinput"
done

popd >/dev/null
