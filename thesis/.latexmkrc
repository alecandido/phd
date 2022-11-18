$out_dir = 'auxfiles';

# Thanks https://tex.stackexchange.com/a/460168/144478
add_cus_dep('acn', 'acr', 0, 'makeglossaries');
sub makeglossaries {
  my ($base_name, $path) = fileparse( $_[0] );
  return system "makeglossaries -d '$path' '$base_name'";
}


# vim: set ft=perl:
