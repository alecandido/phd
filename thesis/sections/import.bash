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

  # revert Juan's alias for begin and end equation
  sd '\\be\b' '\\begin{equation}' $input
  sd '\\ee\b' '\\end{equation}' $input

  # revert Juan's alias for begin and end equation
  for style in {bf,it,tt,sc}; do
    sd '\{\\'$style'\b(.*?)\}' '\\text'$style'{$1}' $input
  done

  for sw in {eko,yadism,pineappl,pineko,apfel}; do
    sd -f i '\\text.*?\{\\\w*? *('$sw') *\}' '\\$1' $input
    sed -e 's@\(\\'$sw'\)@\L\1@gi' -i $input
  done

  echo "finished processing $texinput"
done

popd >/dev/null
