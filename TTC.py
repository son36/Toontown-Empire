from sys import argv
from panda3d.core import Vec3
from pandac.PandaModules import loadPrcFileData
loadPrcFileData('configurate', "window-title Toontown Empire")
from direct.directbase import DirectStart
from direct.task import Task
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.controls.GravityWalker import GravityWalker
from direct.showbase import DirectObject
base.disableMouse()

legsAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgs_shorts_legs_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgs_shorts_legs_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgs_shorts_legs_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgs_shorts_legs_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgs_shorts_legs_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgs_shorts_legs_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgs_shorts_legs_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgs_shorts_legs_left.bam'}
 
torsoAnimDict = {'right-hand-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-hand-start.bam', 'firehose': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_firehose.bam', 'rotateL-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_rotateL-putt.bam', 'slip-forward': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_slip-forward.bam', 'catch-eatnrun': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_eatnrun.bam', 'tickle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_tickle.bam', 'water-gun': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_water-gun.bam', 'leverNeutral': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverNeutral.bam', 'swim': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_swim.bam', 'catch-run': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gamerun.bam', 'sad-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_sad-neutral.bam', 'pet-loop': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petloop.bam', 'jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zstart.bam', 'wave': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_wave.bam', 'reel-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reelneutral.bam', 'pole-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_poleneutral.bam', 'bank': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_jellybeanJar.bam', 'scientistGame': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistGame.bam', 'right-hand': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-hand.bam', 'lookloop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_lookloop-putt.bam', 'victory': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_victory-dance.bam', 'lose': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_lose.bam', 'cringe': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_cringe.bam', 'right': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_right.bam', 'headdown-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_headdown-putt.bam', 'conked': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_conked.bam', 'jump': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump.bam', 'into-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_into-putt.bam', 'fish-end': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishEND.bam', 'running-jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zend.bam', 'shrug': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_shrug.bam', 'sprinkle-dust': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_sprinkle-dust.bam', 'hold-bottle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hold-bottle.bam', 'takePhone': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_takePhone.bam', 'melt': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_melt.bam', 'pet-start': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petin.bam', 'look-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_look-putt.bam', 'loop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_loop-putt.bam', 'good-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_good-putt.bam', 'juggle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_juggle.bam', 'run': 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_run.bam', 'pushbutton': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_press-button.bam', 'sidestep-right': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-back-right.bam', 'water': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_water.bam', 'right-point-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-point-start.bam', 'bad-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_bad-putt.bam', 'struggle': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_struggle.bam', 'running-jump': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_running-jump.bam', 'callPet': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_callPet.bam', 'throw': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_pie-throw.bam', 'catch-eatneutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_eat_neutral.bam', 'tug-o-war': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_tug-o-war.bam', 'bow': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_bow.bam', 'swing': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_swing.bam', 'climb': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_climb.bam', 'scientistWork': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistWork.bam', 'think': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_think.bam', 'catch-intro-throw': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gameThrow.bam', 'walk': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_walk.bam', 'down': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_down.bam', 'pole': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_pole.bam', 'periscope': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_periscope.bam', 'duck': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_duck.bam', 'curtsy': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_curtsy.bam', 'jump-land': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zend.bam', 'loop-dig': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_loop_dig.bam', 'angry': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_angry.bam', 'bored': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_bored.bam', 'swing-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_swing-putt.bam', 'pet-end': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_petend.bam', 'spit': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_spit.bam', 'right-point': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_right-point.bam', 'start-dig': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_into_dig.bam', 'castlong': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_castlong.bam', 'confused': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_confused.bam', 'neutral': 'phase_3/models/char/tt_a_chr_dgl_skirt_torso_neutral.bam', 'jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_jump-zhang.bam', 'reel': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reel.bam', 'slip-backward': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_slip-backward.bam', 'sound': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_shout.bam', 'sidestep-left': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_sidestep-left.bam', 'up': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_up.bam', 'fish-again': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishAGAIN.bam', 'cast': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_cast.bam', 'phoneBack': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_phoneBack.bam', 'phoneNeutral': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_phoneNeutral.bam', 'scientistJealous': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistJealous.bam', 'battlecast': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fish.bam', 'sit-start': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_intoSit.bam', 'toss': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_toss.bam', 'happy-dance': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_happy-dance.bam', 'running-jump-squat': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zstart.bam', 'teleport': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_teleport.bam', 'sit': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_sit.bam', 'sad-walk': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_losewalk.bam', 'give-props-start': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_give-props-start.bam', 'book': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_book.bam', 'running-jump-idle': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_leap_zhang.bam', 'scientistEmcee': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_scientistEmcee.bam', 'leverPull': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverPull.bam', 'tutorial-neutral': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_tutorial-neutral.bam', 'badloop-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_badloop-putt.bam', 'give-props': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_give-props.bam', 'hold-magnet': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hold-magnet.bam', 'hypnotize': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_hypnotize.bam', 'left-point': 'phase_3.5/models/char/tt_a_chr_dgl_skirt_torso_left-point.bam', 'leverReach': 'phase_10/models/char/tt_a_chr_dgl_skirt_torso_leverReach.bam', 'feedPet': 'phase_5.5/models/char/tt_a_chr_dgl_skirt_torso_feedPet.bam', 'reel-H': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_reelH.bam', 'applause': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_applause.bam', 'smooch': 'phase_5/models/char/tt_a_chr_dgl_skirt_torso_smooch.bam', 'rotateR-putt': 'phase_6/models/char/tt_a_chr_dgl_skirt_torso_rotateR-putt.bam', 'fish-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_fishneutral.bam', 'push': 'phase_9/models/char/tt_a_chr_dgl_skirt_torso_push.bam', 'catch-neutral': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_gameneutral.bam', 'left': 'phase_4/models/char/tt_a_chr_dgl_skirt_torso_left.bam'}
 
catHead = loader.loadModel('phase_3/models/char/cat-heads-1000.bam')
otherParts = catHead.findAllMatches('**/*long*')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
ntrlMuzzle = catHead.find('**/*muzzle*neutral')
otherParts = catHead.findAllMatches('**/*muzzle*')
for partNum in range(0, otherParts.getNumPaths()):
    part = otherParts.getPath(partNum)
    if part != ntrlMuzzle:
        otherParts.getPath(partNum).removeNode()
catTorso = loader.loadModel('phase_3/models/char/tt_a_chr_dgl_skirt_torso_1000.bam')
catLegs  = loader.loadModel('phase_3/models/char/tt_a_chr_dgs_shorts_legs_1000.bam')
otherParts = catLegs.findAllMatches('**/boots*')+catLegs.findAllMatches('**/shoes')
for partNum in range(0, otherParts.getNumPaths()):
    otherParts.getPath(partNum).removeNode()
 
catBody = Actor({'head':catHead, 'torso':catTorso, 'legs':catLegs},
                {'torso':torsoAnimDict, 'legs':legsAnimDict})
catBody.attach('head', 'torso', 'def_head')
catBody.attach('torso', 'legs', 'joint_hips')
 
gloves = catBody.findAllMatches('**/hands')
ears = catBody.findAllMatches('**/*ears*')
head = catBody.findAllMatches('**/head-*')
sleeves = catBody.findAllMatches('**/sleeves')
shirt = catBody.findAllMatches('**/torso-top')
skirt = catBody.findAllMatches('**/torso-bot')
neck = catBody.findAllMatches('**/neck')
arms = catBody.findAllMatches('**/arms')
legs = catBody.findAllMatches('**/legs')
feet = catBody.findAllMatches('**/feet')
 
bodyNodes = []
bodyNodes += [gloves]
bodyNodes += [head, ears]
bodyNodes += [sleeves, shirt, skirt]
bodyNodes += [neck, arms, legs, feet]
bodyNodes[0].setColor(1, 1, 1, 1)
bodyNodes[1].setColor(0.30, 0.84, 0.94, 1)
bodyNodes[2].setColor(0.30, 0.84, 0.94, 1)
bodyNodes[3].setColor(0.10, 0.34, 0.29, 1)
bodyNodes[4].setColor(0.56, 0.84, 0.33, 1)
bodyNodes[5].setColor(0.56, 0.84, 0.33, 1)
bodyNodes[6].setColor(0.40, 0.84, 0.76, 1)
bodyNodes[7].setColor(0.40, 0.84, 0.76, 1)
bodyNodes[8].setColor(0.18, 0.54, 0.73, 1)
bodyNodes[9].setColor(0.18, 0.54, 0.73, 1)
 
topTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg')
botTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg')
sleeveTex = loader.loadTexture('phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg')
 
bodyNodes[3].setTexture(sleeveTex, 1)
bodyNodes[4].setTexture(topTex, 1)
bodyNodes[5].setTexture(botTex, 1)
 
catBody.reparentTo(render)
 
geom = catBody.getGeomNode()
geom.getChild(0).setSx(0.730000019073)
geom.getChild(0).setSz(0.730000019073)
 
offset = 3.2375
 
base.camera.reparentTo(catBody)
base.camera.setPos(0, -10.0 - offset, offset)
wallBitmask = BitMask32(1)
floorBitmask = BitMask32(2)
base.cTrav = CollisionTraverser()
def getAirborneHeight():
    return offset + 0.025000000000000001
walkControls = GravityWalker(legacyLifter=True)
walkControls.setWallBitMask(wallBitmask)
walkControls.setFloorBitMask(floorBitmask)
walkControls.setWalkSpeed(16.0, 24.0, 8.0, 80.0)
walkControls.initializeCollisions(base.cTrav, catBody, floorOffset=0.025, reach=4.0)
walkControls.setAirborneHeightFunc(getAirborneHeight)
walkControls.enableAvatarControls()
catBody.physControls = walkControls
 
def setWatchKey(key, input, keyMapName):
    def watchKey(active=True):
        if active == True:
            inputState.set(input, True)
            keyMap[keyMapName] = 1
        else:
            inputState.set(input, False)
            keyMap[keyMapName] = 0
    base.accept(key, watchKey, [True])
    base.accept(key+'-up', watchKey, [False])
 
keyMap = {'left':0, 'right':0, 'forward':0, 'backward':0, 'control':0}
 
setWatchKey('arrow_up', 'forward', 'forward')
setWatchKey('control-arrow_up', 'forward', 'forward')
setWatchKey('alt-arrow_up', 'forward', 'forward')
setWatchKey('shift-arrow_up', 'forward', 'forward')
setWatchKey('arrow_down', 'reverse', 'backward')
setWatchKey('control-arrow_down', 'reverse', 'backward')
setWatchKey('alt-arrow_down', 'reverse', 'backward')
setWatchKey('shift-arrow_down', 'reverse', 'backward')
setWatchKey('arrow_left', 'turnLeft', 'left')
setWatchKey('control-arrow_left', 'turnLeft', 'left')
setWatchKey('alt-arrow_left', 'turnLeft', 'left')
setWatchKey('shift-arrow_left', 'turnLeft', 'left')
setWatchKey('arrow_right', 'turnRight', 'right')
setWatchKey('control-arrow_right', 'turnRight', 'right')
setWatchKey('alt-arrow_right', 'turnRight', 'right')
setWatchKey('shift-arrow_right', 'turnRight', 'right')
setWatchKey('control', 'jump', 'control')
 
movingNeutral, movingForward = (False, False)
movingRotation, movingBackward = (False, False)
movingJumping = False
 
def setMovementAnimation(loopName, playRate=1.0):
    global movingNeutral
    global movingForward
    global movingRotation
    global movingBackward
    global movingJumping
    if 'jump' in loopName:
        movingJumping = True
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'run':
        movingJumping = False
        movingForward = True
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    elif loopName == 'walk':
        movingJumping = False
        movingForward = False
        movingNeutral = False
        if playRate == -1.0:
            movingBackward = True
            movingRotation = False
        else:
            movingBackward = False
            movingRotation = True
    elif loopName == 'neutral':
        movingJumping = False
        movingForward = False
        movingNeutral = True
        movingRotation = False
        movingBackward = False
    else:
        movingJumping = False
        movingForward = False
        movingNeutral = False
        movingRotation = False
        movingBackward = False
    ActorInterval(catBody, loopName, playRate=playRate).loop()
 
def handleMovement(task):
    global movingNeutral, movingForward
    global movingRotation, movingBackward, movingJumping
    if keyMap['control'] == 1:
        if keyMap['forward'] or keyMap['backward'] or keyMap['left'] or keyMap['right']:
            if movingJumping == False:
                if catBody.physControls.isAirborne:
                    setMovementAnimation('running-jump-idle')
                else:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
            else:
                if not catBody.physControls.isAirborne:
                    if keyMap['forward']:
                        if movingForward == False:
                            setMovementAnimation('run')
                    elif keyMap['backward']:
                        if movingBackward == False:
                            setMovementAnimation('walk', playRate=-1.0)
                    elif keyMap['left'] or keyMap['right']:
                        if movingRotation == False:
                            setMovementAnimation('walk')
        else:
            if movingJumping == False:
                if catBody.physControls.isAirborne:
                    setMovementAnimation('jump-idle')
                else:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
            else:
                if not catBody.physControls.isAirborne:
                    if movingNeutral == False:
                        setMovementAnimation('neutral')
    elif keyMap['forward'] == 1:
        if movingForward == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('run')
    elif keyMap['backward'] == 1:
        if movingBackward == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('walk', playRate=-1.0)
    elif keyMap['left'] or keyMap['right']:
        if movingRotation == False:
            if not catBody.physControls.isAirborne:
                setMovementAnimation('walk')
    else:
        if not catBody.physControls.isAirborne:
            if movingNeutral == False:
                setMovementAnimation('neutral')
    return Task.cont
 
base.taskMgr.add(handleMovement, 'controlManager')
 
def collisionsOn():
    catBody.physControls.setCollisionsActive(True)
    catBody.physControls.isAirborne = True
def collisionsOff():
    catBody.physControls.setCollisionsActive(False)
    catBody.physControls.isAirborne = True
def toggleCollisions():
    if catBody.physControls.getCollisionsActive():
        catBody.physControls.setCollisionsActive(False)
        catBody.physControls.isAirborne = True
    else:
        catBody.physControls.setCollisionsActive(True)
        catBody.physControls.isAirborne = True
base.accept('f1', toggleCollisions)
catBody.collisionsOn = collisionsOn
catBody.collisionsOff = collisionsOff
catBody.toggleCollisions = toggleCollisions
 
localAvatar = catBody
base.localAvatar = localAvatar
loadTTC = True
if len(argv) > 1:
    filepath = argv[1]
    if '.' in filepath:
        try:
            execfile(filepath)
            loadTTC = False
        except Exception, e:
            loadTTC = False
            print e
    else:
        loadTTC = True
 

if loadTTC == True:
    TTEnvironment = loader.loadModel("phase_4/models/neighborhoods/toontown_central.bam")
    TTEnvironment.reparentTo(render)
    TTEnvironment.setH(90)
    TTSky = loader.loadModel("phase_3.5/models/props/TT_sky.bam")
    TTSky.reparentTo(render)
    TTSky.setScale(1)
    base.setBackgroundColor(0, .55, 1)
    TTGazebo = loader.loadModel("phase_4/models/modules/gazebo.bam")
    TTGazebo.reparentTo(render)
    TTGazebo.setScale(1, 1, 1)
    TTGazebo.setPos(60, 11, -2) 
    TTHall = loader.loadModel("phase_4/models/modules/toonhall.bam")
    TTHall.reparentTo(render)
    TTHall.setScale(1, 1, 1)
    TTHall.setPos(-103, -24, 2)
    TTHall.setHpr(90,0,0)
    TTBank = loader.loadModel("phase_4/models/modules/bank.bam")
    TTBank.reparentTo(render)
    TTBank.setScale(1, 1, 1)
    TTBank.setPos(-57, -53, 2)
    TTBank.setHpr(180,0,0)
    TTLibrary = loader.loadModel("phase_4/models/modules/library.bam")
    TTLibrary.reparentTo(render)
    TTLibrary.setScale(1, 1, 1)
    TTLibrary.setPos(-92, 66, 2)
    TTGSW = loader.loadModel("phase_4/models/modules/Speedway_Tunnel.bam")
    TTGSW.reparentTo(render)
    TTGSW.setScale(1, 1, 1)
    TTGSW.setPos(-25, -175, 3)
    TTGSW.setHpr(25,0,0)
    TTTrolley = loader.loadModel ("phase_4/models/modules/trolley_station_TT.bam")
    TTTrolley.reparentTo(render)
    TTTrolley.setScale(1, 1, 1)
    TTTrolley.setPos(120.94,77.56,0.52)
    TTTrolley.setHpr(-50,0,0)
    TTGagShop = loader.loadModel ("phase_4/models/modules/gagShop_TT.bam")
    TTGagShop.reparentTo(render)
    TTGagShop.setScale(1, 1, 1)
    TTGagShop.setPos(87,88,0.7)
    TTGagShop.setHpr(165,0,0)
    TTSchool = loader.loadModel("phase_4/models/modules/school_house.bam")
    TTSchool.reparentTo(render)
    TTSchool.setScale(1, 1, 1)
    TTSchool.setPos(-129.91, 138.44, 2.49)
    TTSchool.setHpr(45,0,0)
    TTStore = loader.loadModel("phase_4/models/modules/PetShopExterior_TT.bam")
    TTStore.reparentTo(render)
    TTStore.setScale(1, 1, 1)
    TTStore.setPos(124.37, -74.37, 0.5)
    TTStore.setHpr(230.19,0,0)
    TTHQ = loader.loadModel("phase_3.5/models/modules/TTHQTT.bam")
    TTHQ.reparentTo(render)
    TTHQ.setScale(1, 1, 1)
    TTHQ.setPos(-35.03, -32.86, 4)
    TTHQ.setHpr(336.04,0,0)
    TTTunn1 = loader.loadModel("phase_3.5/models/modules/safe_zone_entrance_tunnel_TT.bam")
    TTTunn1.reparentTo(render)
    TTTunn1.setScale(1, 1, 1)
    TTTunn1.setPos(65, -92, 1)
    TTTunn1.setHpr(180,0,0)
    TTTunn2 = loader.loadModel("phase_3.5/models/modules/safe_zone_entrance_tunnel_TT.bam")
    TTTunn2.reparentTo(render)
    TTTunn2.setScale(1, 1, 1)
    TTTunn2.setPos(146, 23, 1)
    TTTunn2.setHpr(-90,0,0)
    TTTunn3 = loader.loadModel("phase_3.5/models/modules/safe_zone_entrance_tunnel_TT.bam")
    TTTunn3.reparentTo(render)
    TTTunn3.setScale(1, 1, 1)
    TTTunn3.setPos(-50, 165, 3.65)
    TTTunn3.setHpr(-28,0,0)
    TTCloth = loader.loadModel("phase_4/models/modules/clothshopTT.bam")
    TTCloth.reparentTo(render)
    TTCloth.setScale(1, 1, 1)
    TTCloth.setPos(-106.26, -160.83, 3)
    TTCloth.setHpr(150,0,0)
    TTParty = loader.loadModel("phase_4/models/modules/TTPartyGate_TT.bam")
    TTParty.reparentTo(render)
    TTParty.setScale(1, 1, 1)
    TTParty.setPos(-77.93, 159.93, 2.60)
    TTParty.setHpr(25,0,0)
    TTDDBoard = loader.loadModel("phase_3.5/models/props/tunnel_sign_orange.bam")
    TTDDBoard.reparentTo(render)
    TTDDBoard.setScale(1.50, 1.50, 1.50)
    TTDDBoard.setPos(44.86, -91.56, 18.50)
    TTDDBoard.setHpr(180,0,0)
    TTDGBoard = loader.loadModel("phase_3.5/models/props/tunnel_sign_orange.bam")
    TTDGBoard.reparentTo(render)
    TTDGBoard.setScale(1.50, 1.50, 1.50)
    TTDGBoard.setPos(-32.82, 155.65, 20.47)
    TTDGBoard.setHpr(332,0,0)
    TTMMBoard = loader.loadModel("phase_3.5/models/props/tunnel_sign_orange.bam")
    TTMMBoard.reparentTo(render)
    TTMMBoard.setScale(1.50, 1.50, 1.50)
    TTMMBoard.setPos(145.65, 3.23, 17.69)
    TTMMBoard.setHpr(270,0,0)
    TTDDPost = loader.loadModel("phase_4/models/props/neighborhood_sign_DD.bam")
    TTDDPost.reparentTo(render)
    TTDDPost.setScale(1, 1, 1)
    TTDDPost.setPos(31.46, -90.09, 0.52)
    TTDDPost.setHpr(0,0,0)
    TTDDPost1 = loader.loadModel("phase_4/models/props/neighborhood_sign_DD.bam")
    TTDDPost1.reparentTo(render)
    TTDDPost1.setScale(1, 1, 1)
    TTDDPost1.setPos(58.43, -90.43, 0.52)
    TTDDPost1.setHpr(180,0,0)
    TTPlant = loader.loadModel("phase_3.5/models/props/big_TTPlanter.bam")
    TTPlant.reparentTo(render)
    TTPlant.setScale(1, 1, 1)
    TTPlant.setPos(-19.26, -48.88, 4.98)
    TTPlant.setHpr(180,0,0)
    TTFountain = loader.loadModel("phase_4/models/props/toontown_central_TTFountain.bam")
    TTFountain.reparentTo(render)
    TTFountain.setScale(1, 1, 1)
    TTFountain.setPos(-93.20, 106.48, 2.50)
    TTFountain.setHpr(0,0,0)
    TTHorse = loader.loadModel("phase_4/models/props/mickey_on_TTHorse.bam")
    TTHorse.reparentTo(render)
    TTHorse.setScale(1, 1, 1)
    TTHorse.setPos(-80.66, -121.02, 2.49)
    TTHorse.setHpr(0,0,0)
    TTPlant2 = loader.loadModel("phase_3.5/models/props/big_TTPlanter.bam")
    TTPlant2.reparentTo(render)
    TTPlant2.setScale(1, 1, 1)
    TTPlant2.setPos(-21.27, 47.62, 4.98)
    TTPlant2.setHpr(180,0,0)
    TTMouse = Actor("phase_3/models/char/mickey-1200.bam",{"wait":"phase_3/models/char/mickey-wait.bam"})
    TTMouse.reparentTo(render)
    TTMouse.loop("wait")
    TTMouse.setPos(-15,12.22,4)
    TTMouse.setHpr(231.34,0,0)
    TTMouse.setScale(1)
   
localAvatar.physControls.placeOnFloor()
 
run()