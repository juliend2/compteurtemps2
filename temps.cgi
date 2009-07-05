#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw(fatalsToBrowser); # afficher les erreurs
use Data::Dumper;
use Time::Simple;
use Time::Piece;
use Time::Simple::Range;

# require 'local::lib';

require "./functions.pl"; # fonctions diverses

print "Content-type:text/html\n\n";
print <<EndHdr;
<html>
<head><title>URL List</title>
<link rel="stylesheet" href="http://192.168.1.100:8888/temps/styles.css" type="text/css" media="screen" title="no title" charset="utf-8"/>
</head>
<body>
<h1>Time</h1>
<ul>
EndHdr
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
	my %splittedfile = split(/(\n[-a-z_ ]+\s?:\n[-0-9h\s]+)/,$file); # get all the hour blobs

	# VIVE PERL :
	my @blocs = grep {!/^$/} %splittedfile;

	# loop into the blocks :
	foreach my $bloc (@blocs) {
		$bloc =~ m/([-a-z ]+)\s?:/i;
		my $title = $1;
		my $totalTime = 0;
		foreach	my $temps (split(/\n/,$bloc)) {
			# pre($temps);
			if ($temps =~ /(\d{1,2}h\d{2}) - (\d{1,2}h\d{2})/) {
				my $debut = $1;
				my $fin   = $2;
				$debut =~ s/h/:/; 
				$fin   =~ s/h/:/;
				$totalTime += &timeDiff( date1 => '20'.$date.' '.$debut, date2 => '20'.$date.' '.$fin );
			}
		}
		print $title. ' : ';
		print int($totalTime / 60) . '<br/>';	
	}
	print '</li>';
}


print <<EndFooter;
</ul>
</body>
</html>
EndFooter
