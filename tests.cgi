#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs
use Data::Dumper;

require "./functions.pl"; # fonctions diverses

print "Content-type:text/html\n\n";
print <<EndHdr;
<html><head><title>URL List</title></head>
<body>
<h2>Test</h2>
<ul>
EndHdr

# print 'joie';
my @array = ('julien', 'julie', 'titi');
my @foo = ();
# LOOPER POUR AJOUTER SELON UNE CONDITION DE REGEX :
# foreach my $i (@array) {
# 	push @foo, $i if ($i =~ /ju/);
# }
# VIVE PERL :
# @foo = grep /ju/, @array;

# LOOPER POUR AJOUTER AVEC UNE MODIFICATION DE REGEX :
# foreach my $i (@array) {
# 	$i =~ s/ju/JU/;
# 	push @foo, $i;
# }
# VIVE PERL :
# @foo = map {s/ju/JU/; $_} @array;

# TOUT METTRE EN MAJ :
# @foo = map {uc} @array;

# pre(Dumper @foo);


# REFERENCES :
my $a = 'joie';
# my %hash = ( a => "b" );
my $hashref = { $a => "b" }; # references

# pre(Dumper %hash);
pre(Dumper $hashref);


print <<EndFooter;
</ul>
</body>
</html>
EndFooter
