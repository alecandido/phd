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

  # translate citations
  sd ':cite:`(.*?)`' '\\cite{$1}' $input

  # translate list items
  sd '^( *)- ' '$1\\item ' $input

  # multiline syntax
  # ----------------

  # translate text styles
  sd -f ms '\*\*(.*?)\*\*' '\\textbf{$1}' $input
  sd -f ms '\*(.*?)\*' '\\textit{$1}' $input
  sd -f ms '``(.*?)``' '\\texttt{$1}' $input

  # translate sections
  sd -f m '\n(.*?)\n--+' '\n\\subsection{$1}' $input

  # translate display math
  sd -f ms '.. math ?::\n?\n(.*?)\n\n' \
'\\begin{align}
  $1
\\end{align}
\n' $input

  # translate admonitions
  for directive in {admonition,note}; do
  sd -f ms '.. '$directive' ?:: ?([^\n]*)\n\n(.*?)\n\n' '\\paragraph{$1} $2\n' $input
  done

  # translate admonitions
  sd -f ms '.. figure:: ([^\n]*)\n.*?\n\n' \
'\\begin{figure}
  \\centering
  \\includegraphics[width=\\hsize]{$1}
\\end{figure}
\n' $input


  echo "finished processing $texinput"
done

popd >/dev/null
