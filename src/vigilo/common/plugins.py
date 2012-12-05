# -*- coding: utf-8 -*-
# Copyright (C) 2006-2012 CS-SI
# License: GNU GPL v2 <http://www.gnu.org/licenses/gpl-2.0.html>

"""
Affiche les éléments appartenant à un point d'entrée.
Permet notamment de lister les extensions d'une application.
"""

import sys
from pkg_resources import working_set
from optparse import OptionParser
from vigilo.common.argparse import prepare_argparse
from vigilo.common.gettext import translate

_ = translate(__name__)

def main():
    """
    Cette fonction est appelée lorsqu'un utilisateur lance la commande
    'vigilo-plugins'.
    Cet utilitaire permet de lister le contenu d'un point d'entrée.
    """
    prepare_argparse()
    parser = OptionParser()
    parser.add_option('-p', '--provider', action="store_true",
        dest="display_provider", default=False,
        help=_("Displays the name and location of the Python package "
                "which provides this feature."))

    opts, args = parser.parse_args()
    # Sans argument, liste les noms des groupes de points d'entrée
    # se rapportant à Vigilo.
    if not args:
        groups = {}
        vigilo_groups = ('vigilo.', 'vigiadmin.', 'vigiboard.', 'vigiconf.',
                         'vigigraph.', 'vigimap.', 'vigirrd.')
        for distro in working_set:
            for group in distro.get_entry_map().keys():
                if group.startswith(vigilo_groups):
                    groups.setdefault(group, [])
                    groups[group].append(
                        distro.project_name + ' ' + distro.version)
        print _("Available entry-points groups:")
        for group in sorted(list(groups)):
            print "-", group,
            if opts.display_provider:
                print "--", _("Provided by:"), \
                      ", ".join(sorted(groups[group])),
            print
        sys.exit(0)

    for ep in working_set.iter_entry_points(args[0]):
        print "-", ep.name,
        if opts.display_provider:
            print "--", _("Provided by:"), ep.dist,
        print
    sys.exit(0)


if __name__ == '__main__':
    main()
