#!/bin/sh
#
# $Id$

cp fabfile.cfg fabfile.cfg~
sed -e 's/^checkout/#checkout/;s/^#[ ]*\(checkout[ ]*=[ ]*trunk\)/\1/;' fabfile.cfg~ > fabfile.cfg
