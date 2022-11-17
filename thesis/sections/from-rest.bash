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
  sd ':math:`(.*?)`' '$ $1$ ' $input
  sd '\$ ' '$' $input

  # translate display math
  sd -f ms '.. math::\n\n(.*?)\n\n' '\\begin{align}\n$1\n\\end{align}\n\n' $input

  # translate sections
  sd -f m '\n(.*?)\n--+' '\n\\subsection{$1}' $input

  # translate admonitions
  sd -f ms '.. admonition:: ([^\n]*)\n\n(.*?)\n\n' '\\paragraph{$1} $2\n' $input

  # translate admonitions
  sd -f ms '\*\*(.*?)\*\*' '\\textbf{$1}' $input
  sd -f ms '\*(.*?)\*' '\\textit{$1}' $input

  echo "finished processing $texinput"
done

popd >/dev/null
