#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs
use Data::Dumper;
use Time::Simple;
use Time::Piece;
use Time::Simple::Range;
use POSIX qw(strftime);
# require 'local::lib';

require "./functions.pl"; # fonctions diverses

print "Content-type:text/html\n\n";
print <<EndHdr;
<html>
<head><title>Calcul de temps dans mes projets</title>
<style>
EndHdr
# hack to include a css into a perl file :
my $filename = './styles.css';
undef $/;
open (FILE,"< $filename") or die "Can't open $filename : $!";
print <FILE>;
close(FILE);
print <<EndHdr;
</style>
</head>
<body>
<h1>Calcul de temps dans mes projets</h1>
<ul>
EndHdr

my %projects = ();
my @files = </Users/juliend2/Desktop/Dropbox/perso/ressources/TEMPS/*.txt>;
foreach my $file (@files) {
	print '<li>';
	$file =~ m/([0-9-]+).txt$/;
	my $date = $1;
	my $filedate = $date;
	$date =~ m/(\d+)-(\d+)-(\d+)/;
	my $year  = $1;
	my $month = $2;
	my $day   = $3;
	print "<h2>";
	formattime(year=>'20'.$year,month=>$month,day=>$day);
	print "</h2>";
	# get the file :
	my $filename = '/Users/juliend2/Desktop/Dropbox/perso/ressources/TEMPS/'.$filedate.'.txt';
	undef $/;
	open (FILE,"< $filename") or die "Can't open $filename : $!";
	my $file = <FILE>;
	close(FILE);

	# split the file :
	my @blocs = ();
	my %splittedfile = split(/(\n[-a-z0-9,._\(\) ]+\s?:\n[-0-9h\s]+)/,$file); # get all the hour blobs

	# VIVE PERL :
	my @blocs = grep {!/^$/} %splittedfile;

	# loop into the blocks :
	foreach my $bloc (@blocs) {
		$bloc =~ m/([-a-z0-9,._\(\) ]+)\s?:/i;
		my $title = $1;
		my $totalTime = 0;
		foreach	my $temps (split(/\n/,$bloc)) {
			# pre($temps);
			if ($temps =~ /(\d{1,2}h\d{2}) - (\d{1,2}h\d{2})/) {
				my $debut = $1;
				my $fin   = $2;
				$debut =~ s/h/:/; 
				$fin   =~ s/h/:/;
				if (int($debut) <= int($fin)) {
					$totalTime += &timeDiff( date1 => '20'.$date.' '.$debut, date2 => '20'.$date.' '.$fin );
				}
			}
		}
		my $shorttitle = lc($title);
		$shorttitle =~ m/^([-a-z]+)/;
		$shorttitle = $1;
		$projects{$shorttitle} += $totalTime; # ajouter au hash le titre du projet et son temps
		print '<span>';
		print $title. ' : ';
		print '<small>';
		print '<strong><big>'.int($totalTime / 60 / 60).'h'. (int(($totalTime / 60) % 60)<9?'0'.int(($totalTime / 60) % 60):int(($totalTime / 60) % 60)) .'</big></strong><br/>';	
		print '('.int($totalTime / 60) . 'min.)';
		print '</small>';
		print '</span>';
	}
	print '</li>';
}
print '</ul>';

print '<div id="projects">';

my @sortorder = sort keys %projects;
foreach my $key (@sortorder)
{
  print "$key : " . int($projects{$key} / 60)." minutes or <strong>". int($projects{$key} / 60 / 60) ." hours</strong><br/>";
}
print '</div>';

# my $date = '2008-08-10';
# my $fmt = "%A";  # %a = abbreviated weekday %u = weekday number	
# my $mday = substr($date, 8, 2);
# my $mon =  substr($date, 5 ,2);
# my $year = substr($date, 0 ,4);
# my $weekday =
#  strftime($fmt, 0, 0, 0, $mday , $mon - 1, $year - 1900, -1, -1, -1);
# print "$weekday";

# pre(%projects);
print <<EndFooter;
</body>
</html>
EndFooter

# FORMAT DU TEMPS DANS LES FICHIERS QU'ON PARSE :
# Autoprevention (debug utf-8 excel) :
# 	9h55 - 10h20
# 	18h20 - 18h30
# 
# louis (demenager serveur) :
# 	11h10 - 11h30
# 
# VendreQuebec (design) :
# 	12h10 - 12h30
# 	14h15 - 15h00
# 	15h30 - 15h40
# 	15h45 - 15h50
# 
# louis (demenager serveur) :
# 	16h35 - 16h45
# 	16h50 - 17h10
