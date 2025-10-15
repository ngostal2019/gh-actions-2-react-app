const core =  require('@actions/core');
const github = require('@actions/github');
const exec = require('@actions/exec');

function run() {
    // 1) Get some input values
    const bucketName = core.getInput('bucket-name', { require: true });
    const bucketRegion = core.getInput('bucket-region', { require: true });
    const distFolder = core.getInput('dist-folder', { require: true });

    // 2) Upload files to S3
    const s3Uri = `s3://${bucketName}`;
    exec.exec(`aws s3 sync ${distFolder} ${s3Uri} --region ${bucketRegion}`);
    core.notice('Hello from custom JS actions.');

    // 3) Form AWS static Website URL
    const websiteUrl = `http://${bucketName}.s3-website-${bucketRegion}.amazonaws.com`;
    core.setOutput('website-url', websiteUrl);
}

run();