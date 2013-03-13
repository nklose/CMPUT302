
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TK_API = 258,
     TK_AUTOPYNAME = 259,
     TK_DEFDOCSTRING = 260,
     TK_DEFENCODING = 261,
     TK_PLUGIN = 262,
     TK_VIRTERRORHANDLER = 263,
     TK_DOCSTRING = 264,
     TK_DOC = 265,
     TK_EXPORTEDDOC = 266,
     TK_EXTRACT = 267,
     TK_MAKEFILE = 268,
     TK_ACCESSCODE = 269,
     TK_GETCODE = 270,
     TK_SETCODE = 271,
     TK_PREINITCODE = 272,
     TK_INITCODE = 273,
     TK_POSTINITCODE = 274,
     TK_UNITCODE = 275,
     TK_UNITPOSTINCLUDECODE = 276,
     TK_MODCODE = 277,
     TK_TYPECODE = 278,
     TK_PREPYCODE = 279,
     TK_COPYING = 280,
     TK_MAPPEDTYPE = 281,
     TK_CODELINE = 282,
     TK_IF = 283,
     TK_END = 284,
     TK_NAME_VALUE = 285,
     TK_PATH_VALUE = 286,
     TK_STRING_VALUE = 287,
     TK_VIRTUALCATCHERCODE = 288,
     TK_TRAVERSECODE = 289,
     TK_CLEARCODE = 290,
     TK_GETBUFFERCODE = 291,
     TK_RELEASEBUFFERCODE = 292,
     TK_READBUFFERCODE = 293,
     TK_WRITEBUFFERCODE = 294,
     TK_SEGCOUNTCODE = 295,
     TK_CHARBUFFERCODE = 296,
     TK_PICKLECODE = 297,
     TK_METHODCODE = 298,
     TK_INSTANCECODE = 299,
     TK_FROMTYPE = 300,
     TK_TOTYPE = 301,
     TK_TOSUBCLASS = 302,
     TK_INCLUDE = 303,
     TK_OPTINCLUDE = 304,
     TK_IMPORT = 305,
     TK_EXPHEADERCODE = 306,
     TK_MODHEADERCODE = 307,
     TK_TYPEHEADERCODE = 308,
     TK_MODULE = 309,
     TK_CMODULE = 310,
     TK_CONSMODULE = 311,
     TK_COMPOMODULE = 312,
     TK_CLASS = 313,
     TK_STRUCT = 314,
     TK_PUBLIC = 315,
     TK_PROTECTED = 316,
     TK_PRIVATE = 317,
     TK_SIGNALS = 318,
     TK_SIGNAL_METHOD = 319,
     TK_SLOTS = 320,
     TK_SLOT_METHOD = 321,
     TK_BOOL = 322,
     TK_SHORT = 323,
     TK_INT = 324,
     TK_LONG = 325,
     TK_FLOAT = 326,
     TK_DOUBLE = 327,
     TK_CHAR = 328,
     TK_WCHAR_T = 329,
     TK_VOID = 330,
     TK_PYOBJECT = 331,
     TK_PYTUPLE = 332,
     TK_PYLIST = 333,
     TK_PYDICT = 334,
     TK_PYCALLABLE = 335,
     TK_PYSLICE = 336,
     TK_PYTYPE = 337,
     TK_PYBUFFER = 338,
     TK_VIRTUAL = 339,
     TK_ENUM = 340,
     TK_SIGNED = 341,
     TK_UNSIGNED = 342,
     TK_SCOPE = 343,
     TK_LOGICAL_OR = 344,
     TK_CONST = 345,
     TK_STATIC = 346,
     TK_SIPSIGNAL = 347,
     TK_SIPSLOT = 348,
     TK_SIPANYSLOT = 349,
     TK_SIPRXCON = 350,
     TK_SIPRXDIS = 351,
     TK_SIPSLOTCON = 352,
     TK_SIPSLOTDIS = 353,
     TK_SIPSSIZET = 354,
     TK_NUMBER_VALUE = 355,
     TK_REAL_VALUE = 356,
     TK_TYPEDEF = 357,
     TK_NAMESPACE = 358,
     TK_TIMELINE = 359,
     TK_PLATFORMS = 360,
     TK_FEATURE = 361,
     TK_LICENSE = 362,
     TK_QCHAR_VALUE = 363,
     TK_TRUE_VALUE = 364,
     TK_FALSE_VALUE = 365,
     TK_NULL_VALUE = 366,
     TK_OPERATOR = 367,
     TK_THROW = 368,
     TK_QOBJECT = 369,
     TK_EXCEPTION = 370,
     TK_RAISECODE = 371,
     TK_VIRTERRORCODE = 372,
     TK_EXPLICIT = 373,
     TK_TEMPLATE = 374,
     TK_ELLIPSIS = 375,
     TK_DEFMETATYPE = 376,
     TK_DEFSUPERTYPE = 377,
     TK_PROPERTY = 378,
     TK_FORMAT = 379,
     TK_GET = 380,
     TK_ID = 381,
     TK_KWARGS = 382,
     TK_LANGUAGE = 383,
     TK_LICENSEE = 384,
     TK_NAME = 385,
     TK_OPTIONAL = 386,
     TK_ORDER = 387,
     TK_REMOVELEADING = 388,
     TK_SET = 389,
     TK_SIGNATURE = 390,
     TK_TIMESTAMP = 391,
     TK_TYPE = 392,
     TK_USEARGNAMES = 393,
     TK_ALLRAISEPYEXC = 394,
     TK_DEFERRORHANDLER = 395,
     TK_VERSION = 396
   };
#endif
/* Tokens.  */
#define TK_API 258
#define TK_AUTOPYNAME 259
#define TK_DEFDOCSTRING 260
#define TK_DEFENCODING 261
#define TK_PLUGIN 262
#define TK_VIRTERRORHANDLER 263
#define TK_DOCSTRING 264
#define TK_DOC 265
#define TK_EXPORTEDDOC 266
#define TK_EXTRACT 267
#define TK_MAKEFILE 268
#define TK_ACCESSCODE 269
#define TK_GETCODE 270
#define TK_SETCODE 271
#define TK_PREINITCODE 272
#define TK_INITCODE 273
#define TK_POSTINITCODE 274
#define TK_UNITCODE 275
#define TK_UNITPOSTINCLUDECODE 276
#define TK_MODCODE 277
#define TK_TYPECODE 278
#define TK_PREPYCODE 279
#define TK_COPYING 280
#define TK_MAPPEDTYPE 281
#define TK_CODELINE 282
#define TK_IF 283
#define TK_END 284
#define TK_NAME_VALUE 285
#define TK_PATH_VALUE 286
#define TK_STRING_VALUE 287
#define TK_VIRTUALCATCHERCODE 288
#define TK_TRAVERSECODE 289
#define TK_CLEARCODE 290
#define TK_GETBUFFERCODE 291
#define TK_RELEASEBUFFERCODE 292
#define TK_READBUFFERCODE 293
#define TK_WRITEBUFFERCODE 294
#define TK_SEGCOUNTCODE 295
#define TK_CHARBUFFERCODE 296
#define TK_PICKLECODE 297
#define TK_METHODCODE 298
#define TK_INSTANCECODE 299
#define TK_FROMTYPE 300
#define TK_TOTYPE 301
#define TK_TOSUBCLASS 302
#define TK_INCLUDE 303
#define TK_OPTINCLUDE 304
#define TK_IMPORT 305
#define TK_EXPHEADERCODE 306
#define TK_MODHEADERCODE 307
#define TK_TYPEHEADERCODE 308
#define TK_MODULE 309
#define TK_CMODULE 310
#define TK_CONSMODULE 311
#define TK_COMPOMODULE 312
#define TK_CLASS 313
#define TK_STRUCT 314
#define TK_PUBLIC 315
#define TK_PROTECTED 316
#define TK_PRIVATE 317
#define TK_SIGNALS 318
#define TK_SIGNAL_METHOD 319
#define TK_SLOTS 320
#define TK_SLOT_METHOD 321
#define TK_BOOL 322
#define TK_SHORT 323
#define TK_INT 324
#define TK_LONG 325
#define TK_FLOAT 326
#define TK_DOUBLE 327
#define TK_CHAR 328
#define TK_WCHAR_T 329
#define TK_VOID 330
#define TK_PYOBJECT 331
#define TK_PYTUPLE 332
#define TK_PYLIST 333
#define TK_PYDICT 334
#define TK_PYCALLABLE 335
#define TK_PYSLICE 336
#define TK_PYTYPE 337
#define TK_PYBUFFER 338
#define TK_VIRTUAL 339
#define TK_ENUM 340
#define TK_SIGNED 341
#define TK_UNSIGNED 342
#define TK_SCOPE 343
#define TK_LOGICAL_OR 344
#define TK_CONST 345
#define TK_STATIC 346
#define TK_SIPSIGNAL 347
#define TK_SIPSLOT 348
#define TK_SIPANYSLOT 349
#define TK_SIPRXCON 350
#define TK_SIPRXDIS 351
#define TK_SIPSLOTCON 352
#define TK_SIPSLOTDIS 353
#define TK_SIPSSIZET 354
#define TK_NUMBER_VALUE 355
#define TK_REAL_VALUE 356
#define TK_TYPEDEF 357
#define TK_NAMESPACE 358
#define TK_TIMELINE 359
#define TK_PLATFORMS 360
#define TK_FEATURE 361
#define TK_LICENSE 362
#define TK_QCHAR_VALUE 363
#define TK_TRUE_VALUE 364
#define TK_FALSE_VALUE 365
#define TK_NULL_VALUE 366
#define TK_OPERATOR 367
#define TK_THROW 368
#define TK_QOBJECT 369
#define TK_EXCEPTION 370
#define TK_RAISECODE 371
#define TK_VIRTERRORCODE 372
#define TK_EXPLICIT 373
#define TK_TEMPLATE 374
#define TK_ELLIPSIS 375
#define TK_DEFMETATYPE 376
#define TK_DEFSUPERTYPE 377
#define TK_PROPERTY 378
#define TK_FORMAT 379
#define TK_GET 380
#define TK_ID 381
#define TK_KWARGS 382
#define TK_LANGUAGE 383
#define TK_LICENSEE 384
#define TK_NAME 385
#define TK_OPTIONAL 386
#define TK_ORDER 387
#define TK_REMOVELEADING 388
#define TK_SET 389
#define TK_SIGNATURE 390
#define TK_TIMESTAMP 391
#define TK_TYPE 392
#define TK_USEARGNAMES 393
#define TK_ALLRAISEPYEXC 394
#define TK_DEFERRORHANDLER 395
#define TK_VERSION 396




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
{

/* Line 1676 of yacc.c  */
#line 176 "/home/bob/hg/sip/sip-4.14.5-snapshot-c65a525a0a17/sipgen/parser.y"

    char            qchar;
    char            *text;
    long            number;
    double          real;
    argDef          memArg;
    signatureDef    signature;
    signatureDef    *optsignature;
    throwArgs       *throwlist;
    codeBlock       *codeb;
    valueDef        value;
    valueDef        *valp;
    optFlags        optflags;
    optFlag         flag;
    scopedNameDef   *scpvalp;
    fcallDef        fcall;
    int             boolean;
    exceptionDef    exceptionbase;
    classDef        *klass;
    apiCfg          api;
    autoPyNameCfg   autopyname;
    compModuleCfg   compmodule;
    consModuleCfg   consmodule;
    defDocstringCfg defdocstring;
    defEncodingCfg  defencoding;
    defMetatypeCfg  defmetatype;
    defSupertypeCfg defsupertype;
    exceptionCfg    exception;
    docstringCfg    docstring;
    extractCfg      extract;
    featureCfg      feature;
    licenseCfg      license;
    importCfg       import;
    includeCfg      include;
    moduleCfg       module;
    pluginCfg       plugin;
    propertyCfg     property;
    variableCfg     variable;
    vehCfg          veh;
    int             token;



/* Line 1676 of yacc.c  */
#line 378 "/home/bob/hg/sip/sip-4.14.5-snapshot-c65a525a0a17/sipgen/parser.h"
} YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


