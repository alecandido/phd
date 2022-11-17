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
    # ask user for confirmation: switch commented lines to silence
    read -p "Command definitions detected. Are you sure to continue? " -n 1 -r
    # REPLY='y'
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      continue
    fi
  fi

  # scope all labels and references
  sd '(\\label\{.*?):' '$1/'$CHAPTER':' $input
  sd '(\\.?ref\{.*?):' '$1/'$CHAPTER':' $input
  # revert accidental multiple applications of scope
  sd '(\\.*?(ref|label)\{.*?)(/dis)*:' '$1/'$CHAPTER':' $input

  # revert Juan's alias for begin and end equation
  sd '\\be\b' '\\begin{equation}' $input
  sd '\\ee\b' '\\end{equation}' $input

  # revert Juan's alias for brackets
  sd '\\lp\b' '\\left(' $input
  sd '\\rp\b' '\\right)' $input
  sd '\\lc\b' '\\left[' $input
  sd '\\rc\b' '\\right]' $input
  sd '\\la\b' '\\left\\langle' $input
  sd '\\ra\b' '\\right\\rangle' $input

  # upgrade old syntax for font styles
  for style in {bf,it,tt,sc}; do
    sd '\{\\'$style'\b(.*?)\}' '\\text'$style'{$1}' $input
  done

  # replace some software names with corresponding macros
  for sw in {eko,yadism,pineappl,pineko,apfel}; do
    sd -f i '\\text.*?\{\\\w*? *('$sw') *\}' '\\$1' $input
    sed -e 's@\(\\'$sw'\)@\L\1@gi' -i $input
  done

  # replace common patterns
  sd '\bPDF(s?)\b' '\pdf{}$1' $input

  echo "finished processing $texinput"
done

popd >/dev/null
