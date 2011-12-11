#!/usr/bin/python

import sys

import libvhd


def vhd_create(filename, size, disk_type=None, create_flags=None):
    """Usage: <filename> <size> [<disk_type>] [<create_flags>]"""

    return libvhd.vhd_create(filename, size, disk_type=disk_type,
            create_flags=create_flags)


def vhd_convert_from_raw(src_filename, dest_filename, disk_type=None,
        extra=None):
    """Usage: <src_filename> <dest_filename> [<"disk_type">] [<"sparse">]"""

    if disk_type == "sparse" and extra is None:
        extra = disk_type
        disk_type = None
    if extra == "sparse":
        sparse = True
    else:
        sparse = False
    return libvhd.vhd_convert_from_raw(src_filename, dest_filename,
            disk_type=disk_type,
            sparse=sparse)


def vhd_convert_to_raw(src_filename, dest_filename, extra=None):
    """Usage: <src_filename> <dest_filename> [<"sparse">]"""

    if extra == 'sparse':
        sparse = True
    else:
        sparse = False
    return libvhd.vhd_convert_to_raw(src_filename, dest_filename,
            sparse=sparse)


def vhd_print(filename):
    """Usage: <filename>"""

    vhd = libvhd.VHD(filename, 'rdonly')
    footer = vhd.get_footer()
    for name, val in footer.iteritems():
        print "%s: %s" % (name, val)


if __name__ == "__main__":
    args = sys.argv[:]
    prog_name = args.pop(0)

    commands = {
            'create': vhd_create,
            'raw_to_vhd': vhd_convert_from_raw,
            'vhd_to_raw': vhd_convert_to_raw,
            'print': vhd_print}

    def _get_usage(fn):
        doc = fn.__doc__
        for x in doc.split('\n'):
            if x.startswith("Usage: "):
                return x[7:]
        return ""

    def _usage(cmd=None):
        if cmd is not None:
            print "Usage:"
            cmds = {cmd: commands[cmd]}
        else:
            print "Usage: %s <command> [<args>]" % prog_name
            print "Valid commands:"
            cmds = commands
        for cmd, fn in cmds.iteritems():
            print "    %s [<options>] %s" % (cmd, _get_usage(fn))

    if len(args) == 0:
        _usage()
        sys.exit(0)

    cmd = args.pop(0)
    try:
        cmd_fn = commands[cmd]
    except KeyError:
        print "Error: Invalid command"
        _usage()
        sys.exit(1)

    try:
        cmd_fn(*args)
    except TypeError, e:
        error_str = str(e)
        if (error_str.find(cmd_fn.__name__) > -1 and
                error_str.find('takes') > -1):
            print "Error: Invalid arguments"
            _usage(cmd)
            sys.exit(1)
        raise
    except libvhd.VHDException, e:
        _usage(cmd)
        print "Error: %s" % str(e)
        sys.exit(1)
    sys.exit(0)
