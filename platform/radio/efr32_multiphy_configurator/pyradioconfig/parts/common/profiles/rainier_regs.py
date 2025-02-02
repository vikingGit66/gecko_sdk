from pycalcmodel.core.output import ModelOutput, ModelOutputType
from pyradioconfig.parts.common.profiles.bobcat_regs import build_modem_regs_bobcat


def build_modem_regs_rainier(model, profile):
    build_modem_regs_bobcat(model, profile)
    build_synth_regs_s3(model, profile)

    profile.outputs.append(ModelOutput(model.vars.MODEM_TXCORR_TXDGAIN6DB, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXCORR.TXDGAIN6DB'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXCORR_TXDGAIN             , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXCORR.TXDGAIN'                    ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXCORR_TXGAINIMB           , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXCORR.TXGAINIMB'                  ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXCORR_TXPHSIMB            , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXCORR.TXPHSIMB'                   ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_TXFREQCORR_TXFREQCORR      , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXFREQCORR.TXFREQCORR'                 ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_FORCECLKEN          , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.FORCECLKEN'                 ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXIQIMBEN           , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXIQIMBEN'                  ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXINTPEN            , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXINTPEN'                   ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDSEN              , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDSEN'                     ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXIQSWAP            , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXIQSWAP'                   ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDACFORMAT         , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDACFORMAT'                ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDCI               , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDCI'                      ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDCQ               , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDCQ'                      ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_BR2M                , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.BR2M'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXMOD               , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXMOD'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDOFORCEI          , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDOFORCEI'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXMISC_TXDOFORCEQ          , '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXMISC.TXDOFORCEQ'                       ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_TXDACVAL_TXFORCEDI          , '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXDACVAL.TXFORCEDI'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXDACVAL_TXFORCEDQ          , '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXDACVAL.TXFORCEDQ'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXDACVAL_TXIDLEI            , '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXDACVAL.TXIDLEI'                       ))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TXDACVAL_TXIDLEQ            , '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TXDACVAL.TXIDLEQ'                       ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNC2_SYNC2, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNC2.SYNC2'                       ))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EXPECTPATTDUAL_EXPECTPATTDUAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EXPECTPATTDUAL.EXPECTPATTDUAL'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_COCURRMODE_DSSSCONCURRENT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COCURRMODE.DSSSCONCURRENT'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_EHDSSSEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.EHDSSSEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DSSSTIMEACQUTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DSSSTIMEACQUTHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_FOEBIAS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.FOEBIAS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_FREQCORREN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.FREQCORREN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DSSSFRQLIM, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DSSSFRQLIM'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DSSSDSATHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DSSSDSATHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DUALDSA, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DUALDSA'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG0_DSSSPATT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG0.DSSSPATT'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG1_DSSSEXPSYNCLEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG1.DSSSEXPSYNCLEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG1_DSSSCORRTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG1.DSSSCORRTHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG1_DSSSDSAQTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG1.DSSSDSAQTHD'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_DSSSTIMCORRTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.DSSSTIMCORRTHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_DSSSFRTCORRTHD, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.DSSSFRTCORRTHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_DSSSTRACKINGWIN,'', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.DSSSTRACKINGWIN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_DSSSCORRSCHWIN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.DSSSCORRSCHWIN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_ONESYMBOLMBDD,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.ONESYMBOLMBDD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_MAXSCHMODE,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.MAXSCHMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG2_DSSSDSAQUALEN,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG2.DSSSDSAQUALEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG3_DSSSDASMAXTHD,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG3.DSSSDASMAXTHD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG3_DSSSFOETRACKGEAR,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG3.DSSSFOETRACKGEAR'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG3_OPMODE,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG3.OPMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCFG3_DSSSINITIMLEN,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCFG3.DSSSINITIMLEN'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_TRECSCFG_SOFTD,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TRECSCFG.SOFTD'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_TRECSCFG_SDSCALE,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.TRECSCFG.SDSCALE'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_DUALTIM_DUALTIMEN,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DUALTIM_DUALTIMEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DUALTIM_MINCOSTTHD2,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DUALTIM_MINCOSTTHD2'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DUALTIM_SYNCACQWIN2,  '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DUALTIM_SYNCACQWIN2'))



    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_SIMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.SIMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_NOISETHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.NOISETHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_PEAKNUMTHRESHLW, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.PEAKNUMTHRESHLW'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_PEAKNUMADJ, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.PEAKNUMADJ'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_NOISETHRESHADJ, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.NOISETHRESHADJ'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_FREQNOMINAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.FREQNOMINAL'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL0_NDFOCAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL0.NDFOCAL'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_SUPERCHIPTOLERANCE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.SUPERCHIPTOLERANCE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_SMALLSAMPLETHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.SMALLSAMPLETHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_PEAKNUMP2ADJ, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.PEAKNUMP2ADJ'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_FASTMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.FASTMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_TWOSYMBEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.TWOSYMBEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_ZCEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.ZCEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_ZCSAMPLETHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.ZCSAMPLETHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_SOFTCLIPBYPASS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.SOFTCLIPBYPASS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_SOFTCLIPTHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.SOFTCLIPTHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SIRSTAGCMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SIRSTAGCMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SIRSTPRSMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SIRSTPRSMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SIRSTCCAMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SIRSTCCAMODE'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_DISSIFRAMEDET, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.DISSIFRAMEDET'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_AGCRSTUPONSI, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.AGCRSTUPONSI'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SHFTWIN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SHFTWIN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SUPERCHIPNUM, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SUPERCHIPNUM'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_CORRNUM, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.CORRNUM'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_NARROWPULSETHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.NARROWPULSETHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_PEAKNUMADJEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.PEAKNUMADJEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICORR_CORRTHRESH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICORR.CORRTHRESH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICORR_CORRTHRESHLOW, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICORR.CORRTHRESHLOW'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICORR_CORRTHRESHUP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICORR.CORRTHRESHUP'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICORR_CORRTHRESH2SYMB, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICORR.CORRTHRESH2SYMB'))

    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTDIVN, '', ModelOutputType.SVD_REG_FIELD,readable_name='RAC.CLKMULTEN1.CLKMULTDIVN'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTDIVR, '', ModelOutputType.SVD_REG_FIELD,readable_name='RAC.CLKMULTEN1.CLKMULTDIVR'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTDIVX, '', ModelOutputType.SVD_REG_FIELD,readable_name='RAC.CLKMULTEN1.CLKMULTDIVX'))
    profile.outputs.append(ModelOutput(model.vars.RAC_TIAEN_TIAENLATCHI, '', ModelOutputType.SVD_REG_FIELD,readable_name='RAC.TIAEN.TIAENLATCHI'))
    profile.outputs.append(ModelOutput(model.vars.RAC_TIAEN_TIAENLATCHQ, '', ModelOutputType.SVD_REG_FIELD,readable_name='RAC.TIAEN.TIAENLATCHQ'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_FWHOPPING, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.FWHOPPING'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PHDMODCTRL_FASTHOPPINGEN, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PHDMODCTRL.FASTHOPPINGEN'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_PHDMODCTRL_CHPWRQUAL, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PHDMODCTRL.CHPWRQUAL'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SRCCHF_CHMUTETIMER, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SRCCHF.CHMUTETIMER'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CMD_HOPPINGSTART, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CMD.HOPPINGSTART'))
    # profile.outputs.append(ModelOutput(model.vars., '', ModelOutputType.SVD_REG_FIELD, readable_name=''))
    profile.outputs.append(ModelOutput(model.vars.MODEM_CTRL3_ANTDIVMODE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.CTRL3.ANTDIVMODE'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_BLEORZB, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.BLEORZB'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_MULTIPHYHOP, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.MULTIPHYHOP'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_HOPPINGSRC, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.HOPPINGSRC'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_RXBRINTSHIFT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.RXBRINTSHIFT'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_DIGMIXCTRL_DSSSCFECOMBO, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DIGMIXCTRL.DSSSCFECOMBO'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNC3_SYNC3, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNC3.SYNC3'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DSSSPMTIMEOUT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DSSSPMTIMEOUT'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_EHDSSSCTRL_DSSSFRMTIMEOUT, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.EHDSSSCTRL.DSSSFRMTIMEOUT'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_COCURRMODE_DSSSDSACHK, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COCURRMODE.DSSSDSACHK'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_COCURRMODE_TRECSDSACHK, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COCURRMODE.TRECSDSACHK'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_COCURRMODE_CORRCHKMUTE, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COCURRMODE.CORRCHKMUTE'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNCBITS2TH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNCBITS2TH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNC0ERRORS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNC0ERRORS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNC1ERRORS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNC1ERRORS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNC2ERRORS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNC2ERRORS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNC3ERRORS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNC2ERRORS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_DUALSYNC, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.DUALSYNC'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_DUALSYNC2TH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.DUALSYNC2TH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNCDET2TH, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNCDET2TH'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SYNCWORDCTRL_SYNCSWFEC, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SYNCWORDCTRL.SYNCSWFEC'))

    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL1_SYMIDENTDIS, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL1.SYMIDENTDIS'))
    profile.outputs.append(ModelOutput(model.vars.MODEM_SICTRL2_SISTARTDELAY, '', ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.SICTRL2.SISTARTDELAY'))

    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTBWCAL, '', ModelOutputType.SVD_REG_FIELD,    readable_name='RAC.CLKMULTEN1.CLKMULTBWCAL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN1_CLKMULTFREQCAL, '', ModelOutputType.SVD_REG_FIELD,  readable_name='RAC.CLKMULTEN1.CLKMULTFREQCAL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTLDFNIB, '', ModelOutputType.SVD_REG_FIELD,   readable_name='RAC.CLKMULTEN0.CLKMULTLDFNIB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTLDMNIB, '', ModelOutputType.SVD_REG_FIELD,   readable_name='RAC.CLKMULTEN0.CLKMULTLDMNIB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTRDNIBBLE, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC.CLKMULTEN0.CLKMULTRDNIBBLE'))
    profile.outputs.append(ModelOutput(model.vars.RAC_CLKMULTEN0_CLKMULTLDCNIB, '', ModelOutputType.SVD_REG_FIELD,   readable_name='RAC.CLKMULTEN0.CLKMULTLDCNIB'))
    profile.outputs.append(ModelOutput(model.vars.RAC_ADCCTRL1_ADCENHALFMODE, '', ModelOutputType.SVD_REG_FIELD,     readable_name='RAC.ADCCTRL1.ADCENHALFMODE'))
    profile.outputs.append(ModelOutput(model.vars.RAC_ADCCTRL0_ADCCLKSEL, '', ModelOutputType.SVD_REG_FIELD,         readable_name='RAC.ADCCTRL0.ADCCLKSEL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_ADCTRIM0_ADCSIDETONEAMP, '', ModelOutputType.SVD_REG_FIELD,    readable_name='RAC.ADCTRIM0.ADCSIDETONEAMP'))
    profile.outputs.append(ModelOutput(model.vars.RAC_ADCEN0_ADCENNEGRES, '', ModelOutputType.SVD_REG_FIELD,         readable_name='RAC.ADCEN0.ADCENNEGRES'))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_LNAMIXRFPKDTHRESHSELHI, '', ModelOutputType.SVD_REG_FIELD,  readable_name='RAC.LNAMIXCTRL1.LNAMIXRFPKDTHRESHSELHI'))
    profile.outputs.append(ModelOutput(model.vars.RAC_LNAMIXCTRL1_LNAMIXRFPKDTHRESHSELLO, '', ModelOutputType.SVD_REG_FIELD, readable_name='RAC_LNAMIXCTRL1_LNAMIXRFPKDTHRESHSELLO'))
    profile.outputs.append(ModelOutput(model.vars.RAC_TIACTRL0_TIATHRPKDHISEL, '', ModelOutputType.SVD_REG_FIELD,            readable_name='RAC.TIACTRL0.TIATHRPKDHISEL'))
    profile.outputs.append(ModelOutput(model.vars.RAC_TIACTRL0_TIATHRPKDLOSEL, '', ModelOutputType.SVD_REG_FIELD,            readable_name='RAC.TIACTRL0.TIATHRPKDLOSEL'))

## Synth_IF Series 3 Reigsters
def build_synth_regs_s3(model, profile):
    ## LPF
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LOCKLPFBWGEAR0, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LOCKLPFBWGEAR0'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LOCKLPFBWGEAR1, '',         ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LOCKLPFBWGEAR1'))

    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR2, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR3, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR4, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR5, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR5'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR6, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR6'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR7, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR7'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR8, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR8'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLRX_RXLOCKLPFBWGEAR9, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLRX.RXLOCKLPFBWGEAR9'))

    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR2, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR3, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR4, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR5, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR5'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR6, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR6'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR7, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR7'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR8, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR8'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRLTX_TXLOCKLPFBWGEAR9, '',     ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRLTX.TXLOCKLPFBWGEAR9'))

    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LOCKLPFBWGEARSLOT, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LOCKLPFBWGEARSLOT'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LPFBWLOADDEL, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LPFBWLOADDEL'))

    ## DSM
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DSMCTRLRX_DEMMODERX, '',             ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DSMCTRLRX.DEMMODERX'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DSMCTRLRX_REQORDERRX, '',            ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DSMCTRLRX.REQORDERRX'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DSMCTRLTX_LSBFORCETX, '',            ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DSMCTRLTX.LSBFORCETX'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DSMCTRLTX_PHISELTX, '',              ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DSMCTRLTX.PHISELTX'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DSMCTRLTX_REQORDERTX, '',            ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.DSMCTRLTX.REQORDERTX'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_QNCCTRL_QNCMODE, '',                 ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.QNCCTRL.QNCMODE'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_QNCCTRL_QNCOFFSET, '',               ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.QNCCTRL.QNCOFFSET'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_QNCCTRL_ENABLEDQNCTIME, '',          ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.QNCCTRL.ENABLEDQNCTIME'))
    ## DENOMINIT
    profile.outputs.append(ModelOutput(model.vars.SYNTH_MMDDENOMINIT_DENOMINIT0, '',         ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.MMDDENOMINIT.DENOMINIT0'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_MMDDENOMINIT_DENOMINIT1, '',         ModelOutputType.SVD_REG_FIELD, readable_name='SYNTH.MMDDENOMINIT.DENOMINIT1'))
    ## HOPPING
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LPFBWDURINGHOP, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LPFBWDURINGHOP'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_DLFCTRL_LPFBWAFTERHOP, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.DLFCTRL.LPFBWAFTERHOP'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_HOPPING_HOPLPFBWGEARSLOT, '',        ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.HOPPING.HOPLPFBWGEARSLOT'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_HOPPING_HOPHCAPDELAY, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.HOPPING.HOPHCAPDELAY'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_HOPPING_HCAPRETIMEEN, '',            ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.HOPPING.HCAPRETIMEEN'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_HOPPING_HCAPRETIMESEL, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.HOPPING.HCAPRETIMESEL'))
    ## LMS
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSENABLEDELAY, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSENABLEDELAY'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEAR0, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEAR0'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEAR1, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEAR1'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEAR2, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEAR2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEAR3, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEAR3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEAR4, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEAR4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_GLMS_GLMSGEARSLOT, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.GLMS.GLMSGEARSLOT'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSENABLEDELAY, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSENABLEDELAY'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEAR0, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEAR0'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEAR1, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEAR1'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEAR2, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEAR2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEAR3, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEAR3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEAR4, '',                   ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEAR4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_PLMS_PLMSGEARSLOT, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.PLMS.PLMSGEARSLOT'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LMSOVERRIDE_GLMSOVERRIDEEN, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LMSOVERRIDE.GLMSOVERRIDEEN'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LMSOVERRIDE_GLMSOVERRIDEVAL, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LMSOVERRIDE.GLMSOVERRIDEVAL'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LMSOVERRIDE_PLMSOVERRIDEEN, '',       ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LMSOVERRIDE.PLMSOVERRIDEEN'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LMSOVERRIDE_PLMSOVERRIDEVAL, '',      ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LMSOVERRIDE.PLMSOVERRIDEVAL'))
    ## FCAL
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION0, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION0'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION1, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION1'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION2, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION3, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION4, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION5, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION5'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION6, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION6'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_COMPANION_COMPANION7, '',             ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.COMPANION.COMPANION7'))
  #  profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE, '',               ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE1, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE1'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE2, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE3, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE4, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_LOCNTCTRL_NUMCYCLE5, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.LOCNTCTRL.NUMCYCLE5'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_NUMCYCLE6, '',               ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.NUMCYCLE6'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_NUMCYCLE7, '',               ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.NUMCYCLE7'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_NUMCYCLE8, '',               ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.NUMCYCLE8'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_NUMCYCLE9, '',               ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.NUMCYCLE9'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_NUMCYCLE10, '',              ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.NUMCYCLE10'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_STEPWAIT, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.STEPWAIT'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT1, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT1'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT2, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT2'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT3, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT3'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT4, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT4'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT5, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT5'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT6, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT6'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT7, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT7'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT8, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT8'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT9, '',           ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT9'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALSTEPWAIT_STEPWAIT10, '',          ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALSTEPWAIT.STEPWAIT10'))
    profile.outputs.append(ModelOutput(model.vars.SYNTH_FCALCTRL_FCALMODE, '',                ModelOutputType.SVD_REG_FIELD, readable_name='MODEM.FCALCTRL.FCALMODE'))